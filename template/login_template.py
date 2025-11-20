# 登录页面HTML模板
LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>登录 - Markdown阅读器</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .login-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 50px 45px;
            border-radius: 20px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.15), 0 0 0 1px rgba(255,255,255,0.1);
            width: 100%;
            max-width: 440px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .login-header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .login-header h1 {
            color: #1a1a1a;
            margin-bottom: 10px;
            font-weight: 600;
            font-size: 26px;
            letter-spacing: -0.5px;
        }

        .login-header p {
            color: #6c757d;
            font-size: 14px;
            font-weight: 400;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #2c3e50;
            font-weight: 500;
            font-size: 14px;
        }

        .form-group input {
            width: 100%;
            padding: 13px 16px;
            border: 1.5px solid #d1d5db;
            border-radius: 8px;
            font-size: 15px;
            transition: all 0.2s ease;
            background-color: #fafbfc;
        }

        .form-group input:focus {
            outline: none;
            border-color: #2a5298;
            background-color: white;
            box-shadow: 0 0 0 3px rgba(42, 82, 152, 0.08);
        }
        
        .login-btn {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 16px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }

        .login-btn:before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }

        .login-btn:hover:before {
            left: 100%;
        }

        .login-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }

        .login-btn:disabled {
            background: #9ca3af;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        
        .error {
            color: #dc3545;
            background-color: #f8d7da;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
            font-size: 14px;
        }
        
        .security-info {
            margin-top: 25px;
            padding: 18px;
            background-color: #f8f9fb;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
            font-size: 12px;
            color: #6b7280;
            line-height: 1.8;
        }

        .security-info h4 {
            margin-bottom: 10px;
            color: #374151;
            font-weight: 600;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-header">
            <h1>安全登录</h1>
            <p>Markdown 阅读器 - 安全访问</p>
        </div>
        
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
        
        <form id="loginForm">
            <div class="form-group">
                <label for="password">密码：</label>
                <input type="password" id="password" name="password" required 
                       placeholder="请输入密码" autocomplete="current-password">
            </div>
            
            <button type="submit" class="login-btn" id="loginBtn">
                <span id="btnText">登录</span>
            </button>
        </form>
        
        <div class="security-info">
            <h4>安全说明</h4>
            <p>• 密码使用 RSA-2048 非对称加密传输</p>
            <p>• 所有通信均通过 HTTPS 加密</p>
            <p>• 会话将在 1 小时后自动过期</p>
            <p>• 支持本地图片显示</p>
            <p>• 默认密码：admin123</p>
        </div>
    </div>

    <script>
        const PUBLIC_KEY = `{{ public_key }}`;
        
        async function encryptPassword(password) {
            try {
                const keyData = PUBLIC_KEY.replace(/-----BEGIN PUBLIC KEY-----/, '')
                                        .replace(/-----END PUBLIC KEY-----/, '')
                                        .replace(/\\s/g, '');
                
                const binaryKey = Uint8Array.from(atob(keyData), c => c.charCodeAt(0));
                
                const publicKey = await window.crypto.subtle.importKey(
                    'spki',
                    binaryKey,
                    {
                        name: 'RSA-OAEP',
                        hash: 'SHA-256',
                    },
                    false,
                    ['encrypt']
                );
                
                const encodedPassword = new TextEncoder().encode(password);
                const encrypted = await window.crypto.subtle.encrypt(
                    'RSA-OAEP',
                    publicKey,
                    encodedPassword
                );
                
                return btoa(String.fromCharCode(...new Uint8Array(encrypted)));
            } catch (error) {
                console.error('加密失败:', error);
                throw new Error('密码加密失败');
            }
        }
        
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const password = document.getElementById('password').value;
            const loginBtn = document.getElementById('loginBtn');
            const btnText = document.getElementById('btnText');
            
            if (!password) {
                alert('请输入密码');
                return;
            }
            
            loginBtn.disabled = true;
            btnText.textContent = '加密中...';
            
            try {
                const encryptedPassword = await encryptPassword(password);
                
                btnText.textContent = '登录中...';
                
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        encrypted_password: encryptedPassword
                    })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    window.location.href = '/';
                } else {
                    alert('登录失败: ' + (result.error || '密码错误'));
                }
            } catch (error) {
                console.error('登录错误:', error);
                alert('登录失败: ' + error.message);
            } finally {
                loginBtn.disabled = false;
                btnText.textContent = '登录';
                document.getElementById('password').value = '';
            }
        });
    </script>
</body>
</html>
'''
