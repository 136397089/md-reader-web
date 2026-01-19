# -*- coding: utf-8 -*-
# config.py

PASSWORD = 'admin123'  # 默认密码，可修改
PORT_NUMBER = 5000
SECRET_KEY_FILE = '.secret_key'

CONFIG = {
    'password_hash': None,
    'session_timeout': 10000,
    'max_file_size': 50 * 1024 * 1024,  # 50MB
    'read_timeout': 30,  # 30秒
    'request_timeout': 60,  # 60秒
}

# 支持的图片格式
ALLOWED_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico'}
