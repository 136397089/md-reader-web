# -*- coding: utf-8 -*-
# routes.py

from flask import Blueprint, render_template_string, request, jsonify, session, redirect, url_for, send_file, current_app
import os
import time
import json
import hashlib
import mimetypes
from datetime import datetime, timedelta
import markdown
import shutil

from config import CONFIG, ALLOWED_IMAGE_EXTENSIONS
from utils import is_safe_path, get_safe_path, verify_password, PUBLIC_KEY_PEM
from markdown_services import process_markdown_images, MathExtension
from translations import TRANSLATIONS
from template.main_template import MAIN_TEMPLATE, MATHJAX_CONFIG
from template.login_template import LOGIN_TEMPLATE


def _compute_asset_version():
    """基于 app.css/app.js 内容计算版本指纹，内容变更即自动失效浏览器缓存。"""
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    h = hashlib.md5()
    for name in ('app.css', 'app.js'):
        path = os.path.join(static_dir, name)
        try:
            with open(path, 'rb') as f:
                h.update(f.read())
        except OSError:
            pass
    return h.hexdigest()[:8]


# 静态资源版本号（CSS/JS 外链的 ?v= 参数）
ASSET_VERSION = _compute_asset_version()

bp = Blueprint('main', __name__)

# 装饰器：要求认证
def require_auth(f):
    """装饰器：要求认证"""
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect(url_for('main.login'))
        
        if session.get('login_time'):
            # 如果是记住登录状态，则跳过短时间超时检查
            if not session.get('remember_me'):
                login_time = datetime.fromisoformat(session['login_time'])
                if datetime.now() - login_time > timedelta(seconds=CONFIG['session_timeout']):
                    session.clear()
                    return redirect(url_for('main.login'))
        
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# 请求日志中间件
@bp.before_request
def before_request():
    request.start_time = time.time()
    current_app.logger.info(f"开始请求: {request.method} {request.path} - IP: {request.remote_addr}")

@bp.after_app_request
def set_static_cache(response):
    """app 级钩子：对所有请求生效。
    静态资源（/static/）启用长期强缓存，文件名带版本号 query 参数，
    改版后版本号变化即可绕过缓存。"""
    if request.path.startswith('/static/'):
        response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    return response

# 全局异常处理器
@bp.app_errorhandler(Exception)
def handle_exception(e):
    """全局异常处理器"""
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    # Check if e is HTTP error with code, handled separately usually, but here generic catch
    # Flask handle_exception might catch 404/403 if strictly defined but app_errorhandler(Exception) catches all
    # print(f"未处理的异常: {type(e).__name__}: {str(e)}") 
    current_app.logger.error(f"未处理的异常: {type(e).__name__}: {str(e)}")
    if hasattr(e, 'code') and e.code == 413:
        return jsonify({'error': t['request_too_large']}), 413
    
    # Pass through standard HTTP errors if we want default handling or catch specific ones
    if hasattr(e, 'code') and e.code in [404, 403]:
        return e 
        
    return jsonify({'error': t['server_error']}), 500

@bp.app_errorhandler(404)
def not_found(e):
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    return jsonify({'error': t['page_not_found']}), 404

@bp.app_errorhandler(403)
def forbidden(e):
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    return jsonify({'error': t['access_denied']}), 403

@bp.route('/login')
def login():
    """登录页面"""
    lang = request.args.get('lang', session.get('lang', 'zh'))
    session['lang'] = lang
    
    if session.get('authenticated'):
        return redirect(url_for('main.index'))
    
    error = request.args.get('error')
    t = TRANSLATIONS[lang]
    
    # 将翻译字典转换为JSON字符串传递给前端
    translations_json = json.dumps(t)
    
    return render_template_string(
        LOGIN_TEMPLATE, 
        public_key=PUBLIC_KEY_PEM, 
        error=error,
        t=t,
        lang=lang,
        translations_json=translations_json
    )

@bp.route('/api/save', methods=['POST'])
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

@bp.route('/api/login', methods=['POST'])
def api_login():
    """登录API"""
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    try:
        data = request.get_json()
        encrypted_password = data.get('encrypted_password')
        current_app.logger.info(f"Login attempt received. Encrypted Blob Length: {len(encrypted_password) if encrypted_password else 0}")
        
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

@bp.route('/api/logout', methods=['POST'])
def api_logout():
    """登出API"""
    session.clear()
    return jsonify({'success': True})

@bp.route('/')
@require_auth
def index():
    """主页面"""
    lang = request.args.get('lang', session.get('lang', 'zh'))
    session['lang'] = lang
    t = TRANSLATIONS[lang]
    
    # 将翻译字典转换为JSON字符串传递给前端
    translations_json = json.dumps(t)

    return render_template_string(
        MAIN_TEMPLATE,
        t=t,
        lang=lang,
        translations_json=translations_json,
        mathjax_config=MATHJAX_CONFIG,
        asset_version=ASSET_VERSION
    )

@bp.route('/api/files')
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

@bp.route('/api/markdown')
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
            'file_path': file_path,
            'raw_content': content
        })
        
    except Exception as e:
        return jsonify({'error': f"{t['read_file_failed']}{str(e)}"})

@bp.route('/api/preview', methods=['POST'])
@require_auth
def preview_markdown():
    """预览Markdown内容API"""
    lang = session.get('lang', 'zh')
    t = TRANSLATIONS[lang]
    try:
        data = request.get_json()
        content = data.get('content', '')
        file_path = data.get('file_path', '') # Optional, for image resolution
        
        # 转换Markdown为HTML
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
        if file_path:
             html = process_markdown_images(html, file_path)
        
        return jsonify({
            'html': html
        })
        
    except Exception as e:
        return jsonify({'error': f"{t['server_err_prefix']}{str(e)}"})

@bp.route('/api/image')
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
