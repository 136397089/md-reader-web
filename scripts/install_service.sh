#!/usr/bin/env bash
# 安装 markdown_reader 为 systemd 用户服务

set -euo pipefail

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPTS_DIR")"
SERVICE_NAME="markdown-reader"
SERVICE_FILE="$HOME/.config/systemd/user/${SERVICE_NAME}.service"
DATA_DIR="$(dirname "$PROJECT_DIR")"  # /home/he/code/user_system_tools

UV_BIN="$HOME/.local/bin/uv"
PYTHON_SCRIPT="$PROJECT_DIR/src/markdown_reader.py"

# ── 颜色输出 ──────────────────────────────────────────────────────────────────
green()  { printf '\033[0;32m%s\033[0m\n' "$*"; }
yellow() { printf '\033[0;33m%s\033[0m\n' "$*"; }
red()    { printf '\033[0;31m%s\033[0m\n' "$*"; }

# ── 前置检查 ──────────────────────────────────────────────────────────────────
if [[ ! -x "$UV_BIN" ]]; then
    red "错误: 未找到 uv ($UV_BIN)，请先安装: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

if [[ ! -f "$PYTHON_SCRIPT" ]]; then
    red "错误: 未找到启动脚本: $PYTHON_SCRIPT"
    exit 1
fi

if [[ ! -f "$PROJECT_DIR/pyproject.toml" ]]; then
    red "错误: 未找到 pyproject.toml: $PROJECT_DIR/pyproject.toml"
    exit 1
fi

# ── 安装依赖 ──────────────────────────────────────────────────────────────────
yellow ">> 安装 Python 依赖..."
cd "$PROJECT_DIR"
"$UV_BIN" sync --quiet
green "   依赖安装完成"

# ── 创建 systemd 目录 ─────────────────────────────────────────────────────────
mkdir -p "$HOME/.config/systemd/user"

# ── 写入 service 文件 ─────────────────────────────────────────────────────────
yellow ">> 写入服务文件: $SERVICE_FILE"
cat > "$SERVICE_FILE" <<EOF
[Unit]
Description=Markdown Reader Web Service
After=network.target

[Service]
Type=simple
WorkingDirectory=${PROJECT_DIR}
ExecStart=${UV_BIN} run python ${PYTHON_SCRIPT} --target_folder ${DATA_DIR}
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=default.target
EOF
green "   服务文件已写入"

# ── 重载并启用服务 ────────────────────────────────────────────────────────────
yellow ">> 重载 systemd 用户配置..."
systemctl --user daemon-reload

yellow ">> 启用开机自启..."
systemctl --user enable "${SERVICE_NAME}"

yellow ">> 启动服务..."
systemctl --user start "${SERVICE_NAME}"

# ── 状态反馈 ──────────────────────────────────────────────────────────────────
sleep 1
if systemctl --user is-active --quiet "${SERVICE_NAME}"; then
    green ""
    green "✓ 服务已成功启动！"
    green "  访问地址: http://localhost:5000"
    green ""
    green "常用命令:"
    green "  状态: systemctl --user status ${SERVICE_NAME}"
    green "  日志: journalctl --user -u ${SERVICE_NAME} -f"
    green "  停止: systemctl --user stop ${SERVICE_NAME}"
    green "  禁用: systemctl --user disable ${SERVICE_NAME}"
else
    red "✗ 服务启动失败，查看日志："
    journalctl --user -u "${SERVICE_NAME}" -n 20 --no-pager
    exit 1
fi

# ── 提示 lingering ────────────────────────────────────────────────────────────
if ! loginctl show-user "$USER" 2>/dev/null | grep -q "Linger=yes"; then
    yellow ""
    yellow "提示: 要在用户未登录时也保持服务运行，请执行："
    yellow "  sudo loginctl enable-linger $USER"
fi
