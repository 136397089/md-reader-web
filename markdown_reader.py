# -*- coding: utf-8 -*-

# pip install flask markdown cryptography pillow -i https://pypi.tuna.tsinghua.edu.cn/simple --user
from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file
import markdown
import os
import ssl
import subprocess
import signal
from pathlib import Path
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import base64
import secrets
from datetime import datetime, timedelta
import mimetypes
import re
import argparse
import sys
import logging
from logging.handlers import RotatingFileHandler
import threading
import time
import resource
from template.main_template import MAIN_TEMPLATE, MATHJAX_CONFIG
from template.login_template import LOGIN_TEMPLATE
from template.styles import STYLES
from template.scripts import SCRIPTS
from translations import TRANSLATIONS



PASSWORD = 'admin123'  # 默认密码，可修改
PORT_NUMBER = 5000
app = Flask(__name__)

# 密钥文件路径
SECRET_KEY_FILE = '.secret_key'

def get_or_create_secret_key():
    """获取或创建持久化的密钥"""
    if os.path.exists(SECRET_KEY_FILE):
        try:
            with open(SECRET_KEY_FILE, 'rb') as f:
                return f.read()
        except Exception as e:
            print(f"读取密钥文件失败: {e}")
    
    # 生成新密钥
    key = secrets.token_hex(32).encode('utf-8')
    try:
        with open(SECRET_KEY_FILE, 'wb') as f:
            f.write(key)
    except Exception as e:
        print(f"保存密钥文件失败: {e}")
    return key

app.secret_key = get_or_create_secret_key()
app.permanent_session_lifetime = timedelta(days=30)  # 设置永久会话有效期为30天
app.config['SESSION_COOKIE_NAME'] = 'markdown_reader_session'  # 设置独立的会话Cookie名称，避免与其他服务冲突

# 配置日志
def setup_logging():
    # 创建日志格式
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    
    # 文件处理器 - 10MB, 保留5个备份
    file_handler = RotatingFileHandler(
        'app.log', 
        maxBytes=10*1024*1024, 
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # 获取根日志记录器
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # 设置Flask日志
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    app.logger.setLevel(logging.INFO)

setup_logging()

# 资源监控线程
class MonitorThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.running = True
        
    def run(self):
        logging.info("资源监控线程已启动")
        while self.running:
            try:
                # 获取内存使用情况 (RSS)
                usage = resource.getrusage(resource.RUSAGE_SELF)
                memory_mb = usage.ru_maxrss / 1024  # Linux下单位是KB
                
                # 获取当前活跃线程数
                thread_count = threading.active_count()
                
                logging.info(f"系统状态 - 内存: {memory_mb:.2f}MB, 线程数: {thread_count}")
                
                # 每60秒记录一次
                time.sleep(60)
            except Exception as e:
                logging.error(f"监控线程异常: {e}")
                time.sleep(60)

# 请求日志中间件
@app.before_request
def before_request():
    request.start_time = time.time()
    logging.info(f"开始请求: {request.method} {request.path} - IP: {request.remote_addr}")

@app.after_request
def after_request(response):
    if hasattr(request, 'start_time'):
        duration = time.time() - request.start_time
        logging.info(f"结束请求: {request.method} {request.path} - Status: {response.status_code} - Duration: {duration:.4f}s")
    return response

# 配置请求大小和超时
# app.config['MAX_CONTENT_LENGTH'] = CONFIG['max_file_size']

# 全局异常处理器
@app.errorhandler(Exception)
def handle_exception(e):
    """全局异常处理器"""
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    print(f"未处理的异常: {type(e).__name__}: {str(e)}")
    if hasattr(e, 'code') and e.code == 413:
        return jsonify({'error': t['request_too_large']}), 413
    return jsonify({'error': t['server_error']}), 500

@app.errorhandler(404)
def not_found(e):
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    return jsonify({'error': t['page_not_found']}), 404

@app.errorhandler(403)
def forbidden(e):
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    return jsonify({'error': t['access_denied']}), 403

# 生成RSA密钥对
def generate_key_pair():
    """生成RSA密钥对"""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# 全局密钥对
PRIVATE_KEY, PUBLIC_KEY = generate_key_pair()

# 将公钥转换为PEM格式字符串，用于前端
PUBLIC_KEY_PEM = PUBLIC_KEY.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode('utf-8')

# 配置
CONFIG = {
    'password_hash': None,
    'session_timeout': 10000,
    'max_file_size': 50 * 1024 * 1024,  # 50MB
    'read_timeout': 30,  # 30秒
    'request_timeout': 60,  # 60秒
}

# 支持的图片格式
ALLOWED_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico'}

def is_safe_path(path):
    """检查路径是否安全，防止路径遍历攻击"""
    try:
        # 规范化路径
        normalized = os.path.normpath(path)
        # 检查是否包含危险的路径组件
        if '..' in normalized or normalized.startswith('/') or normalized.startswith('\\'):
            return False
        return True
    except:
        return False

def get_safe_path(base_dir, relative_path):
    """获取安全的绝对路径"""
    if not is_safe_path(relative_path):
        return None
    
    full_path = os.path.join(base_dir, relative_path)
    # 确保路径在基目录内
    try:
        full_path = os.path.abspath(full_path)
        base_dir = os.path.abspath(base_dir)
        if not full_path.startswith(base_dir):
            return None
        return full_path
    except:
        return None

def decrypt_password(encrypted_password_b64):
    """解密密码"""
    try:
        encrypted_password = base64.b64decode(encrypted_password_b64)
        decrypted_password = PRIVATE_KEY.decrypt(
            encrypted_password,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_password.decode('utf-8')
    except Exception as e:
        print(f"解密失败: {e}")
        return None

def verify_password(encrypted_password_b64, stored_password=PASSWORD):
    """验证密码"""
    decrypted_password = decrypt_password(encrypted_password_b64)
    return decrypted_password == stored_password

def require_auth(f):
    """装饰器：要求认证"""
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect(url_for('login'))
        
        if session.get('login_time'):
            # 如果是记住登录状态，则跳过短时间超时检查
            if not session.get('remember_me'):
                login_time = datetime.fromisoformat(session['login_time'])
                if datetime.now() - login_time > timedelta(seconds=CONFIG['session_timeout']):
                    session.clear()
                    return redirect(url_for('login'))
        
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def process_markdown_images(html_content, file_path):
    """处理Markdown中的图片链接，转换为安全的API链接"""
    if not file_path:
        return html_content
    
    # 获取文件所在目录
    file_dir = os.path.dirname(file_path)
    
    # 匹配img标签
    img_pattern = r'<img([^>]*?)src=[\'"](.*?)[\'"]([^>]*?)>'
    
    def replace_img(match):
        pre_attrs = match.group(1)
        src = match.group(2)
        post_attrs = match.group(3)
        
        # 跳过网络图片和data:协议图片
        if src.startswith(('http://', 'https://', 'data:')):
            return match.group(0)
        
        # 跳过绝对路径
        if src.startswith('/'):
            return match.group(0)
        
        # 构建相对于Markdown文件的图片路径
        if file_dir:
            image_path = os.path.join(file_dir, src).replace('\\', '/')
        else:
            image_path = src
        
        # 构建新的API链接
        new_src = f'/api/image?path={image_path}'
        
        return f'<img{pre_attrs}src="{new_src}"{post_attrs}>'
    
    return re.sub(img_pattern, replace_img, html_content)


@app.route('/login')
def login():
    """登录页面"""
    lang = request.args.get('lang', session.get('lang', 'zh'))
    session['lang'] = lang
    
    if session.get('authenticated'):
        return redirect(url_for('index'))
    
    error = request.args.get('error')
    t = TRANSLATIONS[lang]
    
    # 将翻译字典转换为JSON字符串传递给前端
    import json
    translations_json = json.dumps(t)
    
    return render_template_string(
        LOGIN_TEMPLATE, 
        public_key=PUBLIC_KEY_PEM, 
        error=error,
        t=t,
        lang=lang,
        translations_json=translations_json
    )


@app.route('/api/save', methods=['POST'])
@require_auth
def save_markdown():
    """保存Markdown文件API"""
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    try:
        data = request.get_json()
        file_path = data.get('file')
        content = data.get('content')
        
        if not file_path or not content:
            return jsonify({'success': False, 'error': t['missing_params']})
        
        if not is_safe_path(file_path):
            return jsonify({'success': False, 'error': t['invalid_path']})
        
        # 检查文件是否是Markdown文件
        if not file_path.lower().endswith(('.md', '.markdown')):
            return jsonify({'success': False, 'error': t['only_markdown']})
        
        base_dir = os.getcwd()
        full_path = get_safe_path(base_dir, file_path)
        
        if not full_path:
            return jsonify({'success': False, 'error': t['file_path_invalid']})
        
        # 创建备份
        backup_dir = os.path.join(base_dir, '.backups')
        os.makedirs(backup_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(
            backup_dir, 
            f"{os.path.basename(file_path)}.{timestamp}.bak"
        )
        
        # 如果原文件存在，创建备份
        if os.path.exists(full_path):
            import shutil
            shutil.copy2(full_path, backup_file)
        
        # 保存新内容
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return jsonify({'success': True})
            
        except Exception as e:
            return jsonify({'success': False, 'error': f"{t['write_failed']}{str(e)}"})
            
    except Exception as e:
        return jsonify({'success': False, 'error': f"{t['server_err_prefix']}{str(e)}"})


@app.route('/api/login', methods=['POST'])
def api_login():
    """登录API"""
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    try:
        data = request.get_json()
        encrypted_password = data.get('encrypted_password')
        
        if not encrypted_password:
            return jsonify({'success': False, 'error': t['missing_password']})
        
        if verify_password(encrypted_password):
            session['authenticated'] = True
            session['login_time'] = datetime.now().isoformat()
            
            remember_me = data.get('remember_me', False)
            if remember_me:
                session.permanent = True
                session['remember_me'] = True
            else:
                session.permanent = False
                session['remember_me'] = False
                
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': t['password_error']})
            
    except Exception as e:
        print(f"登录错误: {e}")
        return jsonify({'success': False, 'error': t['login_failed']})

@app.route('/api/logout', methods=['POST'])
def api_logout():
    """登出API"""
    session.clear()
    return jsonify({'success': True})

@app.route('/')
@require_auth
def index():
    """主页面"""
    lang = request.args.get('lang', session.get('lang', 'zh'))
    session['lang'] = lang
    t = TRANSLATIONS[lang]
    
    # 将翻译字典转换为JSON字符串传递给前端
    import json
    translations_json = json.dumps(t)
    
    return render_template_string(
        MAIN_TEMPLATE,
        t=t,
        lang=lang,
        translations_json=translations_json,
        mathjax_config=MATHJAX_CONFIG,
        styles=STYLES,
        scripts=SCRIPTS
    )

@app.route('/api/files')
@require_auth
def list_files():
    """获取文件列表API"""
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    try:
        path = request.args.get('path', '')
        
        if not is_safe_path(path):
            return jsonify({'error': t['path_invalid']})
        
        base_dir = os.getcwd()
        full_path = get_safe_path(base_dir, path)
        
        if not full_path or not os.path.exists(full_path):
            return jsonify({'error': t['path_not_exist']})
        
        dir_items = []
        file_items = []
        try:
            for item in sorted(os.listdir(full_path)):
                if item.startswith('.') or item == '__pycache__':
                    continue
                
                item_path = os.path.join(full_path, item)
                relative_path = os.path.join(path, item) if path else item
                relative_path = relative_path.replace('\\', '/')
                
                if os.path.isdir(item_path):
                    dir_items.append({
                        'name': item,
                        'type': 'folder',
                        'path': relative_path
                    })
                elif item.lower().endswith(('.md', '.markdown')):
                    file_items.append({
                        'name': item,
                        'type': 'markdown',
                        'path': relative_path
                    })
                else:
                    continue
            
            items = dir_items + file_items
            
        except PermissionError:
            return jsonify({'error': t['permission_denied']})
        
        return jsonify({
            'current_path': path,
            'items': items
        })
        
    except Exception as e:
        return jsonify({'error': f"{t['server_err_prefix']}{str(e)}"})

@app.route('/api/markdown')
@require_auth
def get_markdown():
    """获取Markdown内容API"""
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    try:
        file_path = request.args.get('file', '')
        
        if not file_path or not is_safe_path(file_path):
            return jsonify({'error': t['file_path_invalid']})
        
        if not file_path.lower().endswith(('.md', '.markdown')):
            return jsonify({'error': t['not_markdown']})
        
        base_dir = os.getcwd()
        full_path = get_safe_path(base_dir, file_path)
        
        if not full_path or not os.path.exists(full_path):
            return jsonify({'error': t['file_not_exist']})
        
        # 检查文件大小
        try:
            file_size = os.path.getsize(full_path)
            if file_size > CONFIG['max_file_size']:
                return jsonify({'error': f"{t['file_too_large']} (>{CONFIG['max_file_size']//1024//1024}MB)"})
        except OSError as e:
            return jsonify({'error': f"{t['info_failed']}{str(e)}"})

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(full_path, 'r', encoding='gbk') as f:
                    content = f.read()
            except Exception as e:
                return jsonify({'error': f"{t['encoding_error']}{str(e)}"})
        except IOError as e:
            return jsonify({'error': f"{t['read_failed']}{str(e)}"})
        
        # 转换Markdown为HTML
        # 使用自定义扩展处理数学公式，避免代码块中的$被误识别
        from markdown.extensions import Extension
        from markdown.inlinepatterns import InlineProcessor
        from markdown.util import AtomicString
        import xml.etree.ElementTree as etree

        class MathInlineProcessor(InlineProcessor):
            def handleMatch(self, m, data):
                el = etree.Element('span')
                el.text = AtomicString(f"${m.group(1)}$")
                el.set('class', 'math-inline')
                return el, m.start(0), m.end(0)

        class MathBlockProcessor(InlineProcessor):
            def handleMatch(self, m, data):
                el = etree.Element('div')
                el.text = AtomicString(f"$${m.group(1)}$$")
                el.set('class', 'math-display')
                return el, m.start(0), m.end(0)

        class MathExtension(Extension):
            def extendMarkdown(self, md):
                # 优先级设置：
                # backtick (代码块) 是 175
                # escape (转义) 是 180
                # 我们设置为 < 175，确保代码块先被处理
                
                # 块级公式 $$...$$
                # 使用[\s\S]匹配任意字符包括换行符
                md.inlinePatterns.register(MathBlockProcessor(r'\$\$([\s\S]+?)\$\$', md), 'math_block', 174)
                
                # 行内公式 $...$
                md.inlinePatterns.register(MathInlineProcessor(r'(?<!\\)\$(?!\$)([\s\S]+?)(?<!\\)\$', md), 'math_inline', 173)

        html = markdown.markdown(
            content,
            extensions=['codehilite', 'tables', 'toc', 'fenced_code', 'extra', MathExtension()],
            extension_configs={
                'codehilite': {
                    'css_class': 'highlight'
                }
            }
        )
        
        # 处理图片链接
        html = process_markdown_images(html, file_path)



        
        return jsonify({
            'html': html,
            'file_path': file_path
        })
        
    except Exception as e:
        return jsonify({'error': f"{t['read_file_failed']}{str(e)}"})

@app.route('/api/image')
@require_auth
def get_image():
    """获取图片文件API"""
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    try:
        image_path = request.args.get('path', '')
        
        if not image_path or not is_safe_path(image_path):
            return jsonify({'error': t['invalid_img_path']}), 400
        
        base_dir = os.getcwd()
        full_path = get_safe_path(base_dir, image_path)
        
        if not full_path or not os.path.exists(full_path):
            return jsonify({'error': t['img_not_exist']}), 404
        
        # 检查文件扩展名
        file_ext = os.path.splitext(full_path)[1].lower()
        if file_ext not in ALLOWED_IMAGE_EXTENSIONS:
            return jsonify({'error': t['unsupported_img']}), 400
        
        # 获取MIME类型
        mime_type, _ = mimetypes.guess_type(full_path)
        if not mime_type or not mime_type.startswith('image/'):
            mime_type = 'image/jpeg'  # 默认MIME类型
        
        try:
            return send_file(
                full_path,
                mimetype=mime_type,
                as_attachment=False,
                conditional=True  # 支持HTTP缓存
            )
        except Exception as e:
            print(f"发送图片文件失败: {e}")
            return jsonify({'error': t['img_read_failed']}), 500
            
    except Exception as e:
        print(f"图片API错误: {e}")
        return jsonify({'error': f"{t['server_err_prefix']}{str(e)}"}), 500

def create_ssl_context():
    """创建SSL上下文"""
    cert_file = 'server.crt'
    key_file = 'server.key'

    if not os.path.exists(cert_file) or not os.path.exists(key_file):
        print("正在生成自签名SSL证书...")
        try:
            cmd = [
                'openssl', 'req', '-x509', '-newkey', 'rsa:4096',
                '-keyout', key_file, '-out', cert_file, '-days', '365',
                '-nodes', '-subj', '/C=CN/ST=State/L=City/O=Organization/CN=localhost',
                '-addext', 'subjectAltName=DNS:localhost,IP:127.0.0.1,IP:192.168.1.2,IP:1.2.3.4'
            ]
            result = subprocess.run(cmd, timeout=30, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"SSL证书生成失败: {result.stderr}")
        except subprocess.TimeoutExpired:
            raise Exception("SSL证书生成超时")
        except FileNotFoundError:
            raise Exception("未找到openssl命令，请确保已安装OpenSSL")
        except Exception as e:
            print(f"SSL证书生成错误: {e}")
            raise

    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(cert_file, key_file)
        return context
    except Exception as e:
        print(f"SSL上下文创建失败: {e}")
        raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='安全Markdown阅读器')
    parser.add_argument('--target_folder', nargs='?', default=os.getcwd(),
                       help='目标文件夹路径 (默认: 当前目录)')

    args = parser.parse_args()

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
    print("  • HTTPS加密传输")
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
    print(f"  • HTTPS: https://localhost:{PORT_NUMBER}")
    print(f"  • 默认密码: {PASSWORD}")
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
    print("⚠️  注意: 使用自签名证书，浏览器会显示安全警告，请选择继续访问")
    print("按Ctrl+C停止服务")

    try:
        # 启动监控线程
        monitor_thread = MonitorThread()
        monitor_thread.start()
        
        ssl_context = create_ssl_context()

        app.run(
            host='0.0.0.0',
            port=5000,
            debug=False,
            ssl_context=ssl_context,
            threaded=True,  # 启用多线程
            request_handler=None  # 使用默认的Werkzeug服务器
        )
    except Exception as e:
        print(f"服务器启动失败: {e}")
        exit(1)
    finally:
        print(" -----> mark reader exit...")
