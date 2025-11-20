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
            background: #f8fafc;
            height: 100vh;
            overflow: hidden;
        }

        .app-container {
            display: flex;
            height: 100vh;
        }

        .sidebar {
            width: 350px;
            background: white;
            border-right: 1px solid #e5e7eb;
            display: flex;
            flex-direction: column;
            transition: margin-left 0.3s ease;
        }

        .sidebar.hidden {
            margin-left: -350px;
        }

        .sidebar-header {
            padding: 28px 24px;
            border-bottom: 1px solid #e5e7eb;
            background: #f9fafb;
        }

        .sidebar-header h2 {
            margin-bottom: 8px;
            color: #111827;
            font-size: 20px;
            font-weight: 700;
            letter-spacing: -0.5px;
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
            background: white;
            padding: 24px 32px;
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: space-between;
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
            background: #374151;
            color: white;
            border: none;
            padding: 12px 18px;
            border-radius: 8px;
            cursor: pointer;
            margin-right: 20px;
            font-size: 14px;
            font-weight: 600;
            transition: background-color 0.2s ease;
        }

        .toggle-sidebar:hover {
            background: #1f2937;
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


        .header h1 {
            margin: 0;
            font-size: 24px;
            font-weight: 700;
            color: #111827;
            letter-spacing: -0.7px;
        }

        .content {
            flex: 1;
            background: white;
            padding: 48px;
            overflow-y: auto;
            margin: 0;
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
            background: #f3f4f6;
            color: #374151;
            transform: none;
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
            background: #374151;
            color: white;
            font-weight: 600;
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
            color: #111827;
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
            border-bottom: 3px solid #e5e7eb;
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
            border-left: 4px solid #374151;
            margin: 1.5em 0;
            padding: 20px 24px;
            color: #6b7280;
            font-style: italic;
            background: #f9fafb;
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
            border-radius: 8px;
            margin: 1.5em 0;
            border: 1px solid #e5e7eb;
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
            transform: translateY(-100%);
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
            transition: transform 0.3s ease;
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



'''