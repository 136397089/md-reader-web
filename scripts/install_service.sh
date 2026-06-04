#!/usr/bin/env bash
# 安装 markdown_reader 为 systemd 用户服务

set -euo pipefail

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPTS_DIR")"
SERVICE_NAME="markdown-reader"
SERVICE_FILE="$HOME/.config/systemd/user/${SERVICE_NAME}.service"

UV_BIN="$HOME/.local/bin/uv"
PYTHON_SCRIPT="$PROJECT_DIR/src/markdown_reader.py"

# ── 默认值 ────────────────────────────────────────────────────────────────────
PORT=5000
TARGET_DIR="$(dirname "$PROJECT_DIR")"  # 默认: /home/he/code/user_system_tools

# ── 颜色输出 ──────────────────────────────────────────────────────────────────
green()  { printf '\033[0;32m%s\033[0m\n' "$*"; }
yellow() { printf '\033[0;33m%s\033[0m\n' "$*"; }
red()    { printf '\033[0;31m%s\033[0m\n' "$*"; }

usage() {
    cat <<USAGE
用法: $(basename "$0") [选项]

选项:
  -p, --port PORT        服务监听端口 (默认: 5000)
  -t, --target DIR       Markdown 文件目标路径 (默认: $(dirname "$PROJECT_DIR"))
  -h, --help             显示帮助信息

示例:
  $(basename "$0")
  $(basename "$0") --port 8080
  $(basename "$0") --port 8080 --target /srv/docs
USAGE
}

# ── 解析参数 ──────────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
    case "$1" in
        -p|--port)
            PORT="${2:?'--port 需要一个值'}"
            shift 2
            ;;
        -t|--target)
            TARGET_DIR="${2:?'--target 需要一个值'}"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            red "未知参数: $1"
            usage
            exit 1
            ;;
    esac
done

# 端口范围校验
if ! [[ "$PORT" =~ ^[0-9]+$ ]] || (( PORT < 1 || PORT > 65535 )); then
    red "错误: 端口必须是 1-65535 之间的整数，当前值: $PORT"
    exit 1
fi

# 目标路径规范化为绝对路径
TARGET_DIR="$(realpath -m "$TARGET_DIR")"

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
ExecStart=${UV_BIN} run python ${PYTHON_SCRIPT} --target_folder ${TARGET_DIR} --port ${PORT}
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
    green "  监听端口: ${PORT}"
    green "  目标路径: ${TARGET_DIR}"
    green "  访问地址: http://localhost:${PORT}"
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
