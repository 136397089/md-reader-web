# CSS样式模板
STYLES = '''
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #1f2937;
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            height: 100vh;
            overflow: hidden;
        }

        .app-container {
            display: flex;
            height: 100vh;
        }

        .sidebar {
            width: 350px;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(148, 163, 184, 0.2);
            display: flex;
            flex-direction: column;
            transition: margin-left 0.3s ease;
            box-shadow: 4px 0 20px rgba(0,0,0,0.05);
        }

        .sidebar.hidden {
            margin-left: -350px;
        }

        .sidebar-header {
            padding: 28px 24px;
            border-bottom: 1px solid rgba(148, 163, 184, 0.2);
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        }

        .sidebar-header h2 {
            margin-bottom: 8px;
            color: #111827;
            font-size: 20px;
            font-weight: 700;
            letter-spacing: -0.5px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .sidebar-content {
            flex: 1;
            overflow-y: auto;
            padding: 15px;
        }

        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            min-width: 0;
        }

        .header {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(20px);
            padding: 24px 32px;
            border-bottom: 1px solid rgba(148, 163, 184, 0.2);
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        }

        .header-left {
            display: flex;
            align-items: center;
        }

        .header-right {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .toggle-sidebar {
            background: linear-gradient(135deg, #374151 0%, #1f2937 100%);
            color: white;
            border: none;
            padding: 12px 18px;
            border-radius: 12px;
            cursor: pointer;
            margin-right: 20px;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(55, 65, 81, 0.2);
        }

        .toggle-sidebar:hover {
            background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(55, 65, 81, 0.3);
        }

        .logout-btn {
            background: #dc2626;
            color: white;
            border: none;
            padding: 9px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        .logout-btn:hover {
            background: #b91c1c;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(220, 38, 38, 0.2);
        }

        .user-info {
            color: #6b7280;
            font-size: 13px;
            font-weight: 500;
        }

        .security-badge {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            padding: 8px 14px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
        }

        .math-badge {
            background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
            color: white;
            padding: 8px 14px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 12px rgba(14, 165, 233, 0.3);
        }

        .image-badge {
            background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
            color: white;
            padding: 8px 14px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
        }

        .header h1 {
            margin: 0;
            font-size: 24px;
            font-weight: 700;
            color: #111827;
            letter-spacing: -0.7px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .content {
            flex: 1;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(20px);
            padding: 48px;
            overflow-y: auto;
            margin: 0;
            border-radius: 0 0 0 24px;
        }

        .sidebar .file-list {
            list-style: none;
        }

        .file-item {
            padding: 14px 18px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-bottom: 4px;
            font-size: 15px;
            font-weight: 500;
            border: 1px solid transparent;
        }

        .file-item:hover {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.08) 0%, rgba(118, 75, 162, 0.08) 100%);
            border-color: rgba(102, 126, 234, 0.2);
            transform: translateX(4px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.1);
        }

        .file-item.folder {
            font-weight: 600;
            color: #667eea;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        }

        .file-item.markdown {
            color: #10b981;
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, rgba(6, 182, 212, 0.05) 100%);
        }

        .file-item.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: 600;
            border-color: #667eea;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
            transform: translateX(4px);
        }

        .current-path {
            font-size: 12px;
            color: #6b7280;
            margin-bottom: 15px;
            padding: 10px 12px;
            background-color: #f9fafb;
            border-radius: 6px;
            border: 1px solid #e5e7eb;
            font-family: 'SF Mono', 'Monaco', 'Courier New', monospace;
        }

        .markdown-content {
            line-height: 1.8;
            max-width: none;
        }

        .markdown-content h1,
        .markdown-content h2,
        .markdown-content h3,
        .markdown-content h4,
        .markdown-content h5,
        .markdown-content h6 {
            margin-top: 2.5em;
            margin-bottom: 1.2em;
            color: #111827;
            font-weight: 700;
            letter-spacing: -0.5px;
            line-height: 1.2;
        }

        .markdown-content h1 {
            font-size: 2.5em;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .markdown-content h2 {
            font-size: 2em;
            color: #374151;
        }

        .markdown-content h3 {
            font-size: 1.3em;
        }

        .markdown-content h4 {
            font-size: 1.2em;
        }

        .markdown-content h5 {
            font-size: 1.1em;
        }

        .markdown-content h6 {
            font-size: 1em;
            font-weight: 700;
        }

        .markdown-content h1 {
            border-bottom: 3px solid transparent;
            border-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%) 1;
            padding-bottom: 16px;
        }

        .markdown-content pre {
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 16px 20px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 1.5em 0;
            border: 1px solid #3e3e42;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.4;
            position: relative;
        }

        .markdown-content pre code {
            background: transparent;
            color: inherit;
            padding: 0;
            border-radius: 0;
            border: none;
            font-family: inherit;
            font-size: inherit;
        }

        .markdown-content code {
            background: #f6f8fa;
            color: #24292f;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 0.875em;
            border: 1px solid #d1d9e0;
        }

        .markdown-content blockquote {
            border-left: 5px solid transparent;
            border-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%) 1;
            margin: 1.5em 0;
            padding: 20px 24px;
            color: #6b7280;
            font-style: italic;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
            border-radius: 0 12px 12px 0;
            position: relative;
        }

        .markdown-content blockquote:before {
            content: '"';
            position: absolute;
            top: 10px;
            left: -5px;
            font-size: 4em;
            color: rgba(102, 126, 234, 0.3);
            font-family: Georgia, serif;
            line-height: 1;
        }

        .markdown-content table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }

        .markdown-content th,
        .markdown-content td {
            border: 1px solid #e5e7eb;
            padding: 10px 14px;
            text-align: left;
        }

        .markdown-content th {
            background-color: #f9fafb;
            font-weight: 600;
            color: #111827;
        }

        /* 图片样式优化 */
        .markdown-content img {
            max-width: 100%;
            height: auto;
            border-radius: 16px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
            margin: 1.5em 0;
            cursor: zoom-in;
            transition: all 0.4s ease;
            border: 1px solid rgba(148, 163, 184, 0.2);
        }

        .markdown-content img:hover {
            transform: scale(1.02) translateY(-4px);
            box-shadow: 0 16px 32px rgba(0, 0, 0, 0.18);
            border-color: rgba(102, 126, 234, 0.3);
        }


        /* MathJax数学公式样式优化 */
        .markdown-content .MathJax {
            font-size: 1.1em !important;
        }

        .markdown-content .MathJax_Display {
            margin: 1.5em 0 !important;
            text-align: center;
        }

        .markdown-content mjx-container[jax="CHTML"][display="true"] {
            margin: 1.5em 0;
            text-align: center;
        }

        .markdown-content mjx-container[jax="CHTML"] {
            line-height: 1.2;
        }

        /* 数学公式背景高亮 */
        .markdown-content .math-inline {
            background-color: rgba(14, 165, 233, 0.06);
            padding: 3px 6px;
            border-radius: 4px;
            margin: 0 2px;
        }

        .markdown-content .math-display {
            background-color: rgba(14, 165, 233, 0.03);
            padding: 18px;
            border-radius: 8px;
            margin: 1.5em 0;
            border-left: 3px solid #0891b2;
            border: 1px solid #e0f2fe;
        }

        .loading {
            text-align: center;
            color: #6b7280;
            font-style: italic;
            padding: 60px;
            font-size: 15px;
        }

        .error {
            color: #b91c1c;
            background-color: #fee2e2;
            padding: 16px;
            border-radius: 8px;
            margin: 1em 0;
            border: 1px solid #fecaca;
            font-size: 14px;
        }

        .back-button {
            background-color: #374151;
            color: white;
            border: none;
            padding: 8px 14px;
            border-radius: 6px;
            cursor: pointer;
            margin-bottom: 15px;
            font-size: 12px;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        .back-button:hover {
            background-color: #1f2937;
            transform: translateY(-1px);
        }

        .welcome-message {
            text-align: center;
            color: #6b7280;
            padding: 60px 40px;
        }

        .welcome-message h2 {
            margin-bottom: 20px;
            color: #111827;
            font-weight: 600;
            font-size: 26px;
            letter-spacing: -0.5px;
        }

        .welcome-message p {
            font-size: 15px;
            line-height: 1.8;
        }

        .math-examples {
            margin-top: 35px;
            padding: 24px;
            background-color: #f0f9ff;
            border-radius: 8px;
            border-left: 4px solid #0891b2;
            border: 1px solid #e0f2fe;
        }

        .math-examples h3 {
            color: #0c4a6e;
            margin-bottom: 16px;
            font-weight: 600;
            font-size: 16px;
        }

        .math-examples p {
            margin-bottom: 12px;
            font-size: 14px;
            color: #334155;
        }

        .image-examples {
            margin-top: 25px;
            padding: 24px;
            background-color: #faf5ff;
            border-radius: 8px;
            border: 1px solid #f3e8ff;
            border-left: 4px solid #7c3aed;
        }

        .image-examples h3 {
            color: #5b21b6;
            margin-bottom: 16px;
            font-weight: 600;
            font-size: 16px;
        }

        .image-examples p {
            margin-bottom: 12px;
            font-size: 14px;
            color: #334155;
        }

        /* 在已有的style标签内添加 */
        .header.hidden {
            margin-top: -65px;
            /* 根据header的实际高度调整 */
            overflow: hidden;
        }

        .toggle-header {
            position: fixed;
            top: 0;
            right: 20px;
            background: #374151;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 0 0 6px 6px;
            cursor: pointer;
            z-index: 1000;
            font-size: 12px;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        .toggle-header:hover {
            background: #1f2937;
        }

        .header {
            transition: margin-top 0.3s ease;
        }

        /* 响应式设计 */
        @media (max-width: 768px) {
            .sidebar {
                width: 280px;
            }

            .sidebar.hidden {
                margin-left: -280px;
            }

            .content {
                padding: 20px 15px;
            }

            .header {
                padding: 15px 20px;
            }

            .header-right {
                flex-direction: column;
                gap: 8px;
            }
        }

        /* 无序列表样式优化 */
        .markdown-content ul {
            margin: 1em 0;
            padding-left: 2em;
            list-style-type: disc;
        }

        .markdown-content ul ul {
            margin: 0.5em 0;
            padding-left: 2em;
            list-style-type: circle;
        }

        .markdown-content ul ul ul {
            padding-left: 2em;
            list-style-type: square;
        }

        .markdown-content li {
            margin: 0.4em 0;
            line-height: 1.6;
            padding-left: 0.3em;
            position: relative;
        }

        .markdown-content li p {
            margin: 0.2em 0;
        }

        .markdown-content p {
            margin: 0.8em 0;
        }

        /* 为包含"- "开头的段落添加项目符号 */
        .markdown-content p[data-list-item="true"] {
            position: relative;
        }

        .markdown-content p[data-list-item="true"]::before {
            content: "•";
            color: #666;
            font-weight: bold;
            position: absolute;
            left: -1em;
            top: 0;
        }

        /* 有序列表样式优化 */
        .markdown-content ol {
            margin: 1em 0;
            padding-left: 2em;
            list-style-type: decimal;
        }

        .markdown-content ol ol {
            margin: 0.5em 0;
            padding-left: 1.5em;
            list-style-type: lower-alpha;
        }

        .markdown-content ol ol ol {
            list-style-type: lower-roman;
        }

        .markdown-content ol li {
            margin: 0.3em 0;
            line-height: 1.6;
            padding-left: 0.2em;
        }

        /* 混合列表样式 */
        .markdown-content li > ul,
        .markdown-content li > ol {
            margin-top: 0.3em;
            margin-bottom: 0.3em;
        }

        /* 列表项内的段落和代码 */
        .markdown-content li code {
            background-color: #f3f4f6;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 0.9em;
        }

        .markdown-content li blockquote {
            margin: 0.5em 0;
            padding-left: 1em;
            border-left: 3px solid #2563eb;
            font-style: italic;
            color: #6b7280;
        }

        /* 滚动条样式 */
        .sidebar-content::-webkit-scrollbar,
        .content::-webkit-scrollbar {
            width: 8px;
        }

        .sidebar-content::-webkit-scrollbar-track,
        .content::-webkit-scrollbar-track {
            background: rgba(248, 250, 252, 0.5);
            border-radius: 4px;
        }

        .sidebar-content::-webkit-scrollbar-thumb,
        .content::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 4px;
            transition: all 0.3s ease;
        }

        .sidebar-content::-webkit-scrollbar-thumb:hover,
        .content::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
        }

        /* 页面加载动画 */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .app-container {
            animation: fadeIn 0.6s ease-out;
        }

        /* 按钮悬停波纹效果 */
        @keyframes ripple {
            0% {
                transform: scale(0);
                opacity: 1;
            }
            100% {
                transform: scale(4);
                opacity: 0;
            }
        }

        .toggle-sidebar,
        .logout-btn {
            position: relative;
            overflow: hidden;
        }

        .toggle-sidebar:active:after,
        .logout-btn:active:after {
            content: '';
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.6);
            transform: scale(0);
            animation: ripple 0.6s linear;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            margin-left: -10px;
            margin-top: -10px;
        }
'''