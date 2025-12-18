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

                        <div class="example-box math">
                            <h3>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
                                  <path d="M11.584 2.376a.75.75 0 01.832 0l9 6a.75.75 0 11-.832 1.248L12 3.901 3.416 9.624a.75.75 0 01-.832-1.248l9-6z" />
                                  <path fill-rule="evenodd" d="M20.25 10.332v9.918H21a.75.75 0 010 1.5H3a.75.75 0 010-1.5h.75v-9.918a.75.75 0 01.634-.74A49.109 49.109 0 0112 9c2.59 0 5.134.367 7.516.94a.75.75 0 01.634.741zM12 10.5c-2.51 0-5.018.332-7.5.964V19.5h15v-8.036A47.609 47.609 0 0012 10.5zM12 11.25a.75.75 0 01.75.75v4.5a.75.75 0 01-1.5 0v-4.5a.75.75 0 01.75-.75zm-3.75.75a.75.75 0 00-1.5 0v4.5a.75.75 0 001.5 0v-4.5zm7.5 0a.75.75 0 00-1.5 0v4.5a.75.75 0 001.5 0v-4.5z" clip-rule="evenodd" />
                                </svg>
                                {{ t['math_examples'] }}
                            </h3>
                            <p><strong>{{ t['inline_math'] }}</strong>{{ t['inline_math_desc'] }}</p>
                            <p><strong>{{ t['block_math'] }}</strong>{{ t['block_math_desc'] }}</p>
                            $$\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}$$
                            <p><strong>{{ t['matrix_example'] }}</strong></p>
                            $$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$$
                            <p><strong>{{ t['sum_example'] }}</strong></p>
                            $$\\sum_{n=1}^{\\infty} \\frac{1}{n^2} = \\frac{\\pi^2}{6}$$
                        </div>

                        <div class="example-box images">
                            <h3>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
                                  <path fill-rule="evenodd" d="M1.5 6a2.25 2.25 0 012.25-2.25h16.5A2.25 2.25 0 0122.5 6v12a2.25 2.25 0 01-2.25 2.25H3.75A2.25 2.25 0 011.5 18V6zM3 16.06V18c0 .414.336.75.75.75h16.5A.75.75 0 0021 18v-1.94l-2.69-2.689a1.5 1.5 0 00-2.12 0l-.88.879.97.97a.75.75 0 11-1.06 1.06l-5.16-5.159a1.5 1.5 0 00-2.12 0L3 16.061zm10.125-7.81a1.125 1.125 0 112.25 0 1.125 1.125 0 01-2.25 0z" clip-rule="evenodd" />
                                </svg>
                                {{ t['image_support'] }}
                            </h3>
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
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
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
                <h2>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.5rem; height: 1.5rem; color: var(--primary);">
                      <path d="M11.25 4.533A9.707 9.707 0 006 3.75a9.753 9.753 0 00-3 9.75 9.753 9.753 0 003 9.75 9.753 9.753 0 005.25-.783v-17.934zm1.5 0v17.934a9.753 9.753 0 005.25.783 9.753 9.753 0 003-9.75 9.753 9.753 0 00-3-9.75 9.707 9.707 0 00-5.25.783z" />
                    </svg>
                    {{ t['file_browser'] }}
                </h2>
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
                <div class="header-top">
                    <div class="header-left">
                        <button class="toggle-sidebar" onclick="toggleSidebar()">
                            <span id="toggleIcon" style="display: flex; align-items: center;">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
                                  <path fill-rule="evenodd" d="M7.72 12.53a.75.75 0 010-1.06l7.5-7.5a.75.75 0 111.06 1.06L9.31 12l6.97 6.97a.75.75 0 11-1.06 1.06l-7.5-7.5z" clip-rule="evenodd" />
                                </svg>
                            </span> 
                            {{ t['files_btn'] }}
                        </button>
                        <h1>{{ t['main_title'] }}</h1>
                    </div>
                    <div class="header-right">
                        <button class="btn-icon" onclick="toggleEditMode()" id="editBtn" title="{{ t['edit'] }}" style="display: none;">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
                              <path d="M21.731 2.269a2.625 2.625 0 00-3.712 0l-1.157 1.157 3.712 3.712 1.157-1.157a2.625 2.625 0 000-3.712zM19.513 8.199l-3.712-3.712-12.15 12.15a5.25 5.25 0 00-1.32 2.214l-.8 2.685a.75.75 0 00.933.933l2.685-.8a5.25 5.25 0 002.214-1.32L19.513 8.2z" />
                            </svg>
                        </button>
                        <button class="btn-icon" onclick="saveFile()" id="saveBtn" title="{{ t['save'] }}" style="display: none;">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
                              <path fill-rule="evenodd" d="M19.5 21a3 3 0 003-3V9a3 3 0 00-3-3h-5.379a.75.75 0 01-.53-.22L11.47 3.66A2.25 2.25 0 009.879 3H4.5a3 3 0 00-3 3v12a3 3 0 003 3h15zM9 12.75a.75.75 0 000 1.5h6a.75.75 0 000-1.5H9z" clip-rule="evenodd" />
                            </svg>
                        </button>
                        <button class="btn-icon" onclick="toggleTheme()" id="themeToggle" title="Toggle Theme">
                            <!-- Icon will be set by JS -->
                        </button>
                        <a href="?lang=zh" class="lang-btn {% if lang == 'zh' %}active{% endif %}">中文</a>
                        <a href="?lang=en" class="lang-btn {% if lang == 'en' %}active{% endif %}">English</a>
                        <span class="user-info">{{ t['authenticated'] }}</span>
                        <button class="logout-btn" onclick="logout()">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1rem; height: 1rem;">
                              <path fill-rule="evenodd" d="M7.5 3.75A1.5 1.5 0 006 5.25v13.5a1.5 1.5 0 001.5 1.5h6a1.5 1.5 0 001.5-1.5V15a.75.75 0 011.5 0v3.75a3 3 0 01-3 3h-6a3 3 0 01-3-3V5.25a3 3 0 013-3h6a3 3 0 013 3V9A.75.75 0 0115 9V5.25a1.5 1.5 0 00-1.5-1.5h-6zm10.72 4.72a.75.75 0 011.06 0l3 3a.75.75 0 010 1.06l-3 3a.75.75 0 11-1.06-1.06l1.72-1.72H9a.75.75 0 010-1.5h10.94l-1.72-1.72a.75.75 0 010-1.06z" clip-rule="evenodd" />
                            </svg>
                            {{ t['logout'] }}
                        </button>
                    </div>
                </div>
                
                <div class="tab-bar-container">
                    <div class="tab-bar" id="tabBar">
                        <!-- Tabs will be injected here -->
                    </div>
                </div>
            </div>

            <div class="content">
                <div class="markdown-wrapper" id="markdownWrapper">
                    <div id="welcome-tab" class="tab-content active">
                        <div class="welcome-message">
{WELCOME_CONTENT}
                        </div>
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