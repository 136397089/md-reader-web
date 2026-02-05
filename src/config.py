# -*- coding: utf-8 -*-
# config.py
 
PASSWORD = 'grant91'  # 默认密码，可修改
PORT_NUMBER = 5000
SECRET_KEY_FILE = '.secret_key'
RSA_PRIVATE_KEY_FILE = '.rsa_private_key.pem'
SSL_CERT_FILE = '.cert.pem'
SSL_KEY_FILE = '.key.pem'

CONFIG = {
    'password_hash': None,
    'session_timeout': 10000,
    'max_file_size': 50 * 1024 * 1024,  # 50MB
    'read_timeout': 30,  # 30秒
    'request_timeout': 60,  # 60秒
}

import logging
logging.basicConfig(level=logging.INFO)
logging.info(f"Config loaded. PASSWORD configured: {'Yes' if PASSWORD else 'No'}")
logging.info(f"RSA_PRIVATE_KEY_FILE: {RSA_PRIVATE_KEY_FILE}")
logging.info(f"SECRET_KEY_FILE: {SECRET_KEY_FILE}")

# 支持的图片格式
ALLOWED_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico'}
