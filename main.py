import webview
import ssl
import os
# 禁用全局 SSL 证书验证（对 Python 的 requests 等有效，但对 WebKit 无效）
ssl._create_default_https_context = ssl._create_unverified_context

# 尝试设置环境变量忽略 WebKit SSL 错误 (对于部分 WebKitGTK 版本有效)
# os.environ['WEBKIT_IGNORE_SSL_ERRORS'] = '1'
# os.environ['G_TLS_GNUTLS_PRIORITY'] = 'NORMAL:%DANGER_CLIMB' # 降低 TLS 安全级别尝试规避

TARGET_URL = 'https://app.heweichong.work'
# TARGET_URL = 'http://127.0.0.1:6100'
# 加载你的网页服务地址
icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'app_icon.png')
window = webview.create_window(
    title='我的桌面应用',
    url=TARGET_URL,
    width=1200,
    height=800,
    resizable=True
)

if __name__ == '__main__':
    # 启动窗口
    # private_mode=False 允许使用 localStorage，解决 Linux 下 null error 问题
    webview.start(debug=False, private_mode=False, icon=icon_path)