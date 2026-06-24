# -*- coding: utf-8 -*-
# config.py

import os

PASSWORD = 'grant91'  # 默认密码，可修改
PORT_NUMBER = 5000

_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY_FILE = os.path.join(_SRC_DIR, '.secret_key')
RSA_PRIVATE_KEY_FILE = os.path.join(_SRC_DIR, '.rsa_private_key.pem')

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
