# 登录页面HTML模板
LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ t['login_title'] }}</title>
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
        .lang-switch {
            position: absolute;
            top: 20px;
            right: 20px;
            display: flex;
            gap: 10px;
        }
        
        .lang-btn {
            background: rgba(255, 255, 255, 0.5);
            border: 1px solid rgba(0, 0, 0, 0.1);
            padding: 5px 10px;
            border-radius: 15px;
            cursor: pointer;
            font-size: 12px;
            color: #555;
            text-decoration: none;
            transition: all 0.2s;
        }
        
        .lang-btn:hover, .lang-btn.active {
            background: #667eea;
            color: white;
            border-color: transparent;
        }
    </style>
</head>
<body>
    <div class="lang-switch">
        <a href="?lang=zh" class="lang-btn {% if lang == 'zh' %}active{% endif %}">中文</a>
        <a href="?lang=en" class="lang-btn {% if lang == 'en' %}active{% endif %}">English</a>
    </div>
    <div class="login-container">
        <div class="login-header">
            <h1>{{ t['secure_login'] }}</h1>
            <p>{{ t['app_subtitle'] }}</p>
        </div>
        
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
        
        <form id="loginForm">
            <div class="form-group">
                <label for="password">{{ t['password_label'] }}</label>
                <input type="password" id="password" name="password" required 
                       placeholder="{{ t['password_placeholder'] }}" autocomplete="current-password">
            </div>
            
            <div class="form-group" style="display: flex; align-items: center; margin-bottom: 20px;">
                <input type="checkbox" id="remember_me" name="remember_me" style="width: auto; margin-right: 10px;">
                <label for="remember_me" style="margin-bottom: 0; cursor: pointer;">{{ t['remember_me'] }}</label>
            </div>
            
            <button type="submit" class="login-btn" id="loginBtn">
                <span id="btnText">{{ t['login_btn'] }}</span>
            </button>
        </form>
        
        <div class="security-info">
            <h4>{{ t['security_info_title'] }}</h4>
            <p>{{ t['security_rsa'] }}</p>
            <p>{{ t['security_session'] }}</p>
            <p>{{ t['security_images'] }}</p>
            <p>{{ t['default_password'] }}</p>
        </div>
    </div>

    <script>
        const PUBLIC_KEY = `{{ public_key }}`;
        const TRANSLATIONS = {{ translations_json|safe }};
        console.log('Translations loaded:', TRANSLATIONS);
        
        // Check for Web Crypto API support
        if (!window.crypto || !window.crypto.subtle) {
            console.warn("Web Crypto API is not available! Switching to Insecure (Base64) Mode.");
            const warningDiv = document.createElement('div');
            warningDiv.className = 'error';
            warningDiv.style.backgroundColor = '#fff3cd';
            warningDiv.style.color = '#856404';
            warningDiv.style.borderColor = '#ffeeba';
            warningDiv.style.fontWeight = 'bold';
            warningDiv.innerHTML = "Warning: Insecure Connection.<br>Password will be sent without encryption.";
            const form = document.getElementById('loginForm');
            form.insertBefore(warningDiv, form.firstChild);
            
            // Do NOT disable the button, just indicate insecure mode
            document.getElementById('btnText').textContent = "Login (Insecure)";
        } else {
             console.log("Web Crypto API is available.");
        }
        
        async function encryptPassword(password) {
            console.log("Starting password encryption...");
            
            // Fallback for non-secure contexts
            if (!window.crypto || !window.crypto.subtle) {
                console.log("Web Crypto unavailable. Using Base64 fallback.");
                return btoa(password);
            }

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
                
                console.log("Password encrypted successfully.");
                return btoa(String.fromCharCode(...new Uint8Array(encrypted)));
            } catch (error) {
                console.error('加密失败:', error);
                // Fallback on error too? Maybe safer to just throw if we expected it to work
                throw new Error(TRANSLATIONS['encryption_failed'] + ": " + error.message);
            }
        }
        
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            console.log("Login form submitted.");
            
            const password = document.getElementById('password').value;
            const rememberMe = document.getElementById('remember_me').checked;
            const loginBtn = document.getElementById('loginBtn');
            const btnText = document.getElementById('btnText');
            
            if (!password) {
                alert(TRANSLATIONS['enter_password']);
                return;
            }
            
            loginBtn.disabled = true;
            btnText.textContent = TRANSLATIONS['encrypting'];
            
            try {
                const encryptedPassword = await encryptPassword(password);
                
                btnText.textContent = TRANSLATIONS['logging_in'];
                console.log("Sending login request...");
                
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        encrypted_password: encryptedPassword,
                        remember_me: rememberMe
                    })
                });
                
                console.log("Response received:", response.status);
                const result = await response.json();
                console.log("Result:", result);
                
                if (result.success) {
                    window.location.href = '/';
                } else {
                    alert(TRANSLATIONS['login_failed'] + ': ' + (result.error || TRANSLATIONS['password_error']));
                }
            } catch (error) {
                console.error('登录错误:', error);
                alert(TRANSLATIONS['login_failed'] + ': ' + error.message);
            } finally {
                loginBtn.disabled = false;
                btnText.textContent = TRANSLATIONS['login_btn'];
                document.getElementById('password').value = '';
            }
        });
    </script>
</body>
</html>
'''
