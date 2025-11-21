# MathJax配置模板
MATHJAX_CONFIG = '''
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\\$', '\\\$']],
                displayMath: [['$$', '$$'], ['\\\$', '\\\$']],
                processEscapes: true,
                processEnvironments: true,
                tags: 'ams',
                macros: {
                    // 常用数学宏定义
                    RR: "\\\\mathbb{R}",
                    NN: "\\\\mathbb{N}",
                    ZZ: "\\\\mathbb{Z}",
                    QQ: "\\\\mathbb{Q}",
                    CC: "\\\\mathbb{C}",
                    dd: "\\\\mathrm{d}",
                    ee: "\\\\mathrm{e}",
                    ii: "\\\\mathrm{i}",
                    jj: "\\\\mathrm{j}",
                    Re: "\\\\operatorname{Re}",
                    Im: "\\\\operatorname{Im}",
                    Tr: "\\\\operatorname{Tr}",
                    rank: "\\\\operatorname{rank}",
                    span: "\\\\operatorname{span}",
                    dim: "\\\\operatorname{dim}",
                    ker: "\\\\operatorname{ker}",
                    det: "\\\\operatorname{det}",
                    gcd: "\\\\operatorname{gcd}",
                    lcm: "\\\\operatorname{lcm}",
                    max: "\\\\operatorname{max}",
                    min: "\\\\operatorname{min}",
                    sup: "\\\\operatorname{sup}",
                    inf: "\\\\operatorname{inf}",
                    lim: "\\\\operatorname{lim}",
                    limsup: "\\\\operatorname{limsup}",
                    liminf: "\\\\operatorname{liminf}"
                }
            },
            svg: {
                fontCache: 'global'
            },
            options: {
                renderActions: {
                    addMenu: [0, '', '']
                }
            },
            startup: {
                ready: () => {
                    MathJax.startup.defaultReady();
                    console.log('MathJax已加载完成');
                }
            }
        };
    </script>

    <!-- 加载MathJax -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
'''

# 欢迎信息内容
WELCOME_CONTENT = '''
                        <h2>{{ t['welcome_title'] }}</h2>
                        <p>{{ t['welcome_msg1'] }}</p>
                        <p>{{ t['welcome_msg2'] }}</p>
                        <p>{{ t['welcome_https'] }}</p>
                        <p>{{ t['welcome_latex'] }}</p>
                        <p>{{ t['welcome_images'] }}</p>

                        <div class="math-examples">
                            <h3>{{ t['math_examples'] }}</h3>
                            <p><strong>{{ t['inline_math'] }}</strong>{{ t['inline_math_desc'] }}</p>
                            <p><strong>{{ t['block_math'] }}</strong>{{ t['block_math_desc'] }}</p>
                            $$\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}$$
                            <p><strong>{{ t['matrix_example'] }}</strong></p>
                            $$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$$
                            <p><strong>{{ t['sum_example'] }}</strong></p>
                            $$\\sum_{n=1}^{\\infty} \\frac{1}{n^2} = \\frac{\\pi^2}{6}$$
                        </div>

                        <div class="image-examples">
                            <h3>{{ t['image_support'] }}</h3>
                            <p><strong>{{ t['support_formats'] }}</strong>{{ t['support_formats_desc'] }}</p>
                            <p><strong>{{ t['relative_path'] }}</strong>![描述](./images/pic.jpg)</p>
                            <p><strong>{{ t['absolute_path'] }}</strong>![描述](/path/to/image.png)</p>
                            <p><strong>{{ t['web_image'] }}</strong>![描述](https://example.com/image.jpg)</p>
                            <p><strong>{{ t['security_features'] }}</strong>{{ t['security_features_desc'] }}</p>
                        </div>
'''

# 主页面HTML模板
# from .styles import STYLES  <-- No longer needed here
# from .scripts import SCRIPTS <-- No longer needed here

MAIN_TEMPLATE = '''
<!DOCTYPE html>
<html lang="{{ lang }}">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ t['main_title'] }}</title>

    <!-- MathJax配置 -->
    {{ mathjax_config|safe }}

    <style>
{{ styles|safe }}
    </style>
</head>

<body>
    <div class="app-container">
        <!-- 固定的隐藏/显示标题栏按钮 -->
        <button class="toggle-header" onclick="toggleHeader()" id="toggleHeaderBtn">
            {{ t['hide_header'] }}
        </button>

        <!-- 左侧文件浏览器 -->
        <div class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h2>{{ t['file_browser'] }}</h2>
            </div>
            <div class="sidebar-content">
                <div class="current-path" id="currentPath">{{ t['current_path'] }}/</div>
                <button class="back-button" id="backButton" onclick="goBack()" style="display: none;">{{ t['back_to_parent'] }}</button>
                <ul class="file-list" id="fileList">
                    <!-- 文件列表将通过JavaScript动态加载 -->
                </ul>
            </div>
        </div>

        <!-- 主内容区域 -->
        <div class="main-content">
            <div class="header">
                <div class="header-left">
                    <button class="toggle-sidebar" onclick="toggleSidebar()">
                        <span id="toggleIcon">◀</span> {{ t['files_btn'] }}
                    </button>
                    <h1>{{ t['main_title'] }}</h1>
                </div>
                <div class="header-right">
                    <a href="?lang=zh" class="lang-btn {% if lang == 'zh' %}active{% endif %}" style="margin-right: 10px; text-decoration: none; color: #555;">中文</a>
                    <a href="?lang=en" class="lang-btn {% if lang == 'en' %}active{% endif %}" style="margin-right: 20px; text-decoration: none; color: #555;">English</a>
                    <span class="user-info">{{ t['authenticated'] }}</span>
                    <button class="logout-btn" onclick="logout()">{{ t['logout'] }}</button>
                </div>

            </div>

            <div class="content">
                <div id="markdownContent">
                    <div class="welcome-message">
{WELCOME_CONTENT}
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const TRANSLATIONS = {{ translations_json|safe }};
{{ scripts|safe }}
    </script>
</body>

</html>
'''