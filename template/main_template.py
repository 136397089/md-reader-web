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
                        <h2>欢迎使用 Markdown 阅读器</h2>
                        <p>请从左侧文件浏览器选择一个 Markdown 文件开始阅读</p>
                        <p>点击左上角的"文件"按钮可以隐藏/显示文件浏览器</p>
                        <p>当前连接已通过 HTTPS 加密保护</p>
                        <p>支持 LaTeX 数学公式渲染</p>
                        <p>支持本地图片显示</p>

                        <div class="math-examples">
                            <h3>数学公式示例</h3>
                            <p><strong>行内公式：</strong>使用单个 $ 符号包围，如 $E = mc^2$</p>
                            <p><strong>块级公式：</strong>使用双 $ 符号包围：</p>
                            $$\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}$$
                            <p><strong>矩阵示例：</strong></p>
                            $$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$$
                            <p><strong>求和公式：</strong></p>
                            $$\\sum_{n=1}^{\\infty} \\frac{1}{n^2} = \\frac{\\pi^2}{6}$$
                        </div>

                        <div class="image-examples">
                            <h3>图片支持说明</h3>
                            <p><strong>支持格式：</strong>JPG, PNG, GIF, BMP, WebP, SVG 等</p>
                            <p><strong>相对路径：</strong>![描述](./images/pic.jpg)</p>
                            <p><strong>绝对路径：</strong>![描述](/path/to/image.png)</p>
                            <p><strong>网络图片：</strong>![描述](https://example.com/image.jpg)</p>
                            <p><strong>安全特性：</strong>自动防护路径遍历攻击，确保文件访问安全</p>
                        </div>
'''

# 主页面HTML模板
from .styles import STYLES
from .scripts import SCRIPTS

MAIN_TEMPLATE = f'''
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown阅读器</title>

    <!-- MathJax配置 -->
    {MATHJAX_CONFIG}

    <style>
{STYLES}
    </style>
</head>

<body>
    <div class="app-container">
        <!-- 固定的隐藏/显示标题栏按钮 -->
        <button class="toggle-header" onclick="toggleHeader()" id="toggleHeaderBtn">
            隐藏标题栏
        </button>

        <!-- 左侧文件浏览器 -->
        <div class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h2>文件浏览器</h2>
            </div>
            <div class="sidebar-content">
                <div class="current-path" id="currentPath">当前路径: /</div>
                <button class="back-button" id="backButton" onclick="goBack()" style="display: none;">← 返回上级</button>
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
                        <span id="toggleIcon">◀</span> 文件
                    </button>
                    <h1>Markdown 阅读器</h1>
                </div>
                <div class="header-right">
                    <span class="user-info">已认证</span>
                    <button class="logout-btn" onclick="logout()">退出登录</button>
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
{SCRIPTS}
    </script>
</body>

</html>
'''