# -*- coding: utf-8 -*-
# utils.py

import os
import secrets
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import datetime
import base64
import logging
from logging.handlers import RotatingFileHandler

from config import SECRET_KEY_FILE, PASSWORD, RSA_PRIVATE_KEY_FILE

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

def get_or_create_key_pair():
    """获取或创建持久化的RSA密钥对"""
    abs_key_path = os.path.abspath(RSA_PRIVATE_KEY_FILE)
    logging.info(f"Using RSA Key File: {abs_key_path}")
    
    if os.path.exists(RSA_PRIVATE_KEY_FILE):
        try:
            with open(RSA_PRIVATE_KEY_FILE, 'rb') as f:
                private_key_data = f.read()
                private_key = serialization.load_pem_private_key(
                    private_key_data,
                    password=None,
                    backend=default_backend()
                )
                public_key = private_key.public_key()
                return private_key, public_key
        except Exception as e:
            print(f"读取RSA密钥文件失败: {e}")
            logging.error(f"Failed to load RSA key file: {e}")
            # 如果读取失败，继续生成新的
    
    print("正在生成新的RSA密钥对...")
    logging.info("Generating new RSA key pair...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    # 保存私钥
    try:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(RSA_PRIVATE_KEY_FILE, 'wb') as f:
            f.write(pem)
        print("RSA密钥对已保存")
        logging.info("RSA key pair saved.")
    except Exception as e:
        print(f"保存RSA密钥文件失败: {e}")
        logging.error(f"Failed to save RSA key file: {e}")
    
    return private_key, public_key

# 全局密钥对
logging.info(f"Initializing global key pair from {RSA_PRIVATE_KEY_FILE}...")
PRIVATE_KEY, PUBLIC_KEY = get_or_create_key_pair()
logging.info("Global key pair initialized.")

# 将公钥转换为PEM格式字符串，用于前端
PUBLIC_KEY_PEM = PUBLIC_KEY.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode('utf-8')

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
        logging.info(f"Attempting to decrypt password (len={len(encrypted_password_b64)})...")
        encrypted_password = base64.b64decode(encrypted_password_b64)
        decrypted_password = PRIVATE_KEY.decrypt(
            encrypted_password,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        result = decrypted_password.decode('utf-8')
        logging.info("Password decrypted successfully.")
        return result
    except Exception as e:
        print(f"解密失败: {e}")
        logging.error(f"Decryption failed: {e}")
        return None
 
def verify_password(encrypted_password_b64, stored_password=PASSWORD):
    """验证密码"""
    logging.info(f"Verifying password against stored (len={len(stored_password)})")
    decrypted_password = decrypt_password(encrypted_password_b64)
    
    if decrypted_password is None:
        logging.warning("Verification failed: Decryption returned None")
        return False
        
    is_match = False
    
    # 1. Try RSA verification
    if decrypted_password is not None:
         is_match = decrypted_password == stored_password
    
    # 2. If failed, try simple Base64 fallback for HTTP mode
    if not is_match:
        logging.info("RSA verification failed or skipped. Attempting Base64 fallback...")
        try:
            # The input is expected to be base64(password) from the frontend in fallback mode
            fallback_password = base64.b64decode(encrypted_password_b64).decode('utf-8')
            if fallback_password == stored_password:
                is_match = True
                logging.info("Base64 fallback verification SUCCESS")
            else:
                logging.warning(f"Base64 fallback verification FAILED. Decoded: {fallback_password[:2]}***")
        except Exception as e:
            logging.warning(f"Base64 fallback decoding failed: {e}")

    if is_match:
        logging.info("Password verification SUCCESS")
    else:
        logging.warning(f"Password verification FAILED.")
        # logging.warning(f"Stored password (len={len(stored_password)}): {stored_password[:2]}***{stored_password[-2:] if len(stored_password)>3 else ''}")
        # logging.warning(f"Decrypted password (len={len(decrypted_password)}): {decrypted_password[:2]}***{decrypted_password[-2:] if len(decrypted_password)>3 else ''}")
        # Optional: Log first/last chars if safe, but length mismatch is usually enough hint
        
    return is_match

def setup_logging(app):
    """配置日志"""
    # 创建日志格式
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    
    # 文件处理器 - 10MB, 保留5个备份
    file_handler = RotatingFileHandler(
        'markdown_reader.log', 
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
