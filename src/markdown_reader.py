# -*- coding: utf-8 -*-
# markdown_reader.py

# pip install flask markdown cryptography pillow -i https://pypi.tuna.tsinghua.edu.cn/simple --user
from flask import Flask
import os
import sys
import argparse
from datetime import timedelta

# Import from new modules
from config import PORT_NUMBER, PASSWORD, SECRET_KEY_FILE
from utils import get_or_create_secret_key, setup_logging
from monitor import MonitorThread
from routes import bp

app = Flask(__name__)

# Config
app.secret_key = get_or_create_secret_key()
app.permanent_session_lifetime = timedelta(days=30)  # 设置永久会话有效期为30天
app.config['SESSION_COOKIE_NAME'] = 'markdown_reader_session'  # 设置独立的会话Cookie名称，避免与其他服务冲突

# 配置日志
setup_logging(app)

# Register Blueprint
app.register_blueprint(bp)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='安全Markdown阅读器')
    parser.add_argument('--target_folder', nargs='?', default=os.getcwd(),
                       help='目标文件夹路径 (默认: 当前目录)')
    parser.add_argument('--port', type=int, default=PORT_NUMBER,
                       help=f'服务监听端口 (默认: {PORT_NUMBER})')

    args = parser.parse_args()
    port = args.port

    # 验证目标文件夹存在
    target_folder = os.path.abspath(args.target_folder)
    if not os.path.exists(target_folder):
        print(f"错误: 目标文件夹不存在: {target_folder}")
        sys.exit(1)

    if not os.path.isdir(target_folder):
        print(f"错误: 指定路径不是文件夹: {target_folder}")
        sys.exit(1)

    # 切换到目标文件夹
    os.chdir(target_folder)

    required_packages = ['markdown', 'cryptography']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print(f"请先安装所需的包: pip install {' '.join(missing_packages)}")
        exit(1)



    print("🔐 安全Markdown阅读器启动中...")
    print("📊 功能特性:")
    print("  • HTTP传输")
    print("  • RSA-2048非对称加密密码验证")
    print("  • LaTeX数学公式支持 (MathJax)")
    print("  • 本地图片显示支持")
    print("  • 路径遍历攻击防护")
    print("  • 会话管理和超时控制")
    print("  • 文件大小限制和请求超时保护")
    print("")
    print(f"📂 目标目录: {target_folder}")
    print("")
    print("🌐 访问地址:")
    print(f"  • HTTP: http://localhost:{port}")
    print(f"  • 默认密码: {PASSWORD}")
    print("")

    print("")
    print("📐 数学公式语法:")
    print("  • 行内公式: $E = mc^2$")
    print("  • 块级公式: $$\\int_0^1 x^2 dx$$")
    print("  • 支持完整LaTeX语法")
    print("")
    print("🖼️ 图片支持:")
    print("  • 支持格式: JPG, PNG, GIF, BMP, WebP, SVG等")
    print("  • 相对路径: ![描述](./images/pic.jpg)")
    print("  • 自动安全检查，防止路径遍历攻击")
    print("  • 点击图片可放大/缩小")
    print("")
    print("按Ctrl+C停止服务")

    try:
        # 启动监控线程
        monitor_thread = MonitorThread()
        monitor_thread.start()

        app.run(
            host='0.0.0.0',
            port=port,
            debug=False,
            threaded=True,  # 启用多线程
            request_handler=None  # 使用默认的Werkzeug服务器
        )
    except Exception as e:
        print(f"服务器启动失败: {e}")
        exit(1)
    finally:
        print(" -----> mark reader exit...")
