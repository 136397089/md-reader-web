# CSS样式模板
STYLES = '''
        :root {
            /* Color Palette - Modern Slate & Indigo Theme */
            --bg-body: #f8fafc;
            --bg-surface: #ffffff;
            --bg-sidebar: #ffffff;
            --bg-header: rgba(255, 255, 255, 0.9);
            
            --text-main: #1e293b;
            --text-muted: #64748b;
            --text-light: #94a3b8;
            
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --primary-light: #e0e7ff;
            
            --border-color: #e2e8f0;
            --border-hover: #cbd5e1;
            
            --success: #10b981;
            --success-bg: #d1fae5;
            --danger: #ef4444;
            --danger-hover: #dc2626;
            
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
            
            --radius-sm: 0.375rem;
            --radius-md: 0.5rem;
            --radius-lg: 0.75rem;
            
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            --font-mono: 'JetBrains Mono', 'SF Mono', 'Monaco', 'Courier New', monospace;
        }

        [data-theme="dark"] {
            --bg-body: #0f172a; /* Slate 900 */
            --bg-surface: #1e293b; /* Slate 800 */
            --bg-sidebar: #1e293b;
            --bg-header: rgba(30, 41, 59, 0.9); /* Slate 800 with opacity */
            
            --text-main: #f1f5f9; /* Slate 100 */
            --text-muted: #94a3b8; /* Slate 400 */
            --text-light: #64748b; /* Slate 500 */
            
            --primary: #818cf8; /* Indigo 400 */
            --primary-hover: #6366f1; /* Indigo 500 */
            --primary-light: rgba(99, 102, 241, 0.15);
            
            --border-color: #334155; /* Slate 700 */
            --border-hover: #475569; /* Slate 600 */
            
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.4), 0 2px 4px -2px rgb(0 0 0 / 0.4);
            --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.4), 0 4px 6px -4px rgb(0 0 0 / 0.4);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-sans);
            line-height: 1.6;
            color: var(--text-main);
            background: var(--bg-body);
            height: 100vh;
            overflow: hidden;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        .app-container {
            display: flex;
            height: 100vh;
        }

        /* Sidebar Styling */
        .sidebar {
            width: 320px;
            background: var(--bg-sidebar);
            border-right: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 20;
        }

        .sidebar.hidden {
            margin-left: -320px;
            opacity: 0;
        }

        .sidebar-header {
            padding: 24px;
            border-bottom: 1px solid var(--border-color);
            background: var(--bg-surface);
        }

        .sidebar-header h2 {
            margin: 0;
            color: var(--text-main);
            font-size: 1.25rem;
            font-weight: 700;
            letter-spacing: -0.025em;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .sidebar-content {
            flex: 1;
            overflow-y: auto;
            padding: 16px;
        }
        
        /* Custom Scrollbar for Sidebar */
        .sidebar-content::-webkit-scrollbar {
            width: 6px;
        }
        .sidebar-content::-webkit-scrollbar-track {
            background: transparent;
        }
        .sidebar-content::-webkit-scrollbar-thumb {
            background-color: var(--border-color);
            border-radius: 20px;
        }

        /* File List Styling */
        .file-list {
            list-style: none;
        }

        .file-item {
            display: flex;
            align-items: center;
            padding: 10px 12px;
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: all 0.2s ease;
            margin-bottom: 2px;
            font-size: 0.95rem;
            color: var(--text-muted);
            font-weight: 500;
            border: 1px solid transparent;
            gap: 10px;
        }

        .file-item:hover {
            background: var(--bg-body);
            color: var(--text-main);
        }

        .file-item.folder {
            color: var(--text-main);
        }
        
        .file-item.folder svg {
            color: #fbbf24; /* Amber 400 for folders */
        }

        .file-item.markdown {
            color: var(--text-main);
        }
        
        .file-item.markdown svg {
            color: var(--primary);
        }

        .file-item.active {
            background: var(--primary-light);
            color: var(--primary);
            font-weight: 600;
        }

        .current-path {
            font-size: 0.75rem;
            color: var(--text-light);
            margin-bottom: 16px;
            padding: 8px 12px;
            background-color: var(--bg-body);
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-color);
            font-family: var(--font-mono);
            word-break: break-all;
        }

        /* Main Content Area */
        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            min-width: 0;
            background: var(--bg-surface);
            position: relative;
        }

        /* Header Styling */
        .header {
            background: var(--bg-header);
            backdrop-filter: blur(8px);
            padding: 0;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            position: sticky;
            top: 0;
            z-index: 10;
            transition: transform 0.3s ease;
        }

        .header-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 32px;
            width: 100%;
        }
        
        .app-container.header-hidden .header {
            transform: translateY(-100%);
        }

        .header-left {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .header-right {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .header h1 {
            margin: 0;
            font-size: 1.125rem;
            font-weight: 600;
            color: var(--text-main);
            letter-spacing: -0.01em;
        }

        /* Buttons */
        .btn-icon {
            background: transparent;
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 8px;
            border-radius: var(--radius-md);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }
        
        .btn-icon:hover {
            background: var(--bg-body);
            color: var(--text-main);
            border-color: var(--border-hover);
        }

        .toggle-sidebar {
            display: flex;
            align-items: center;
            gap: 8px;
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-weight: 500;
            cursor: pointer;
            padding: 6px 10px;
            border-radius: var(--radius-md);
            transition: all 0.2s;
        }

        .toggle-sidebar:hover {
            background: var(--bg-body);
            color: var(--text-main);
        }

        .logout-btn {
            background: var(--danger);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: var(--radius-md);
            cursor: pointer;
            font-size: 0.875rem;
            font-weight: 500;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: var(--shadow-sm);
        }

        .logout-btn:hover {
            background: var(--danger-hover);
            box-shadow: var(--shadow-md);
        }

        .lang-btn {
            text-decoration: none;
            color: var(--text-muted);
            font-size: 0.875rem;
            font-weight: 500;
            padding: 4px 8px;
            border-radius: var(--radius-sm);
            transition: all 0.2s;
        }
        
        .lang-btn:hover {
            color: var(--text-main);
            background: var(--bg-body);
        }
        
        .lang-btn.active {
            color: var(--primary);
            background: var(--primary-light);
        }

        .user-info {
            color: var(--text-light);
            font-size: 0.875rem;
            font-weight: 500;
        }

        /* Content Area */
        .content {
            flex: 1;
            padding: 0;
            overflow-y: auto;
            scroll-behavior: smooth;
        }

        .markdown-wrapper {
            max-width: 860px;
            margin: 0 auto;
            padding: 24px 32px 96px;
        }

        /* Tab Bar Styling */
        .tab-bar-container {
            background: rgba(255, 255, 255, 0.5); /* Slight transparency */
            border-top: 1px solid var(--border-color);
            padding: 0 32px;
            display: flex;
            align-items: center;
            width: 100%;
        }
        
        [data-theme="dark"] .tab-bar-container {
            background: rgba(30, 41, 59, 0.5);
        }
        
        .header.hidden ~ .content .tab-bar-container {
            /* No longer needed as it moves with header */
        }

        .tab-bar {
            display: flex;
            overflow-x: auto;
            scrollbar-width: none; /* Firefox */
            -ms-overflow-style: none;  /* IE 10+ */
            width: 100%;
        }
        
        .tab-bar::-webkit-scrollbar {
            display: none; /* Chrome/Safari */
        }

        .tab {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            cursor: pointer;
            border-right: 1px solid var(--border-color);
            border-bottom: 2px solid transparent;
            background: transparent;
            color: var(--text-muted);
            font-size: 0.85rem;
            font-weight: 500;
            white-space: nowrap;
            transition: all 0.2s;
            max-width: 180px;
        }

        .tab:hover {
            background: var(--bg-body);
            color: var(--text-main);
        }

        .tab.active {
            color: var(--primary);
            border-bottom-color: var(--primary);
            background: var(--bg-surface);
        }

        .tab-icon {
            display: flex;
            align-items: center;
            color: inherit;
            transform: scale(0.9);
        }

        .tab-title {
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .tab-close {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            margin-left: 4px;
            opacity: 0.6;
            transition: all 0.2s;
        }

        .tab-close:hover {
            background: var(--danger-hover);
            color: white;
            opacity: 1;
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
        }


        /* Markdown Typography */
        .markdown-content {
            line-height: 1.75;
            font-size: 1.0625rem;
            color: var(--text-main);
        }

        .markdown-content h1,
        .markdown-content h2,
        .markdown-content h3,
        .markdown-content h4,
        .markdown-content h5,
        .markdown-content h6 {
            color: var(--text-main);
            font-weight: 700;
            line-height: 1.3;
            margin-top: 2em;
            margin-bottom: 0.8em;
            letter-spacing: -0.025em;
        }

        .markdown-content h1 {
            font-size: 2.25rem;
            padding-bottom: 0.5em;
            border-bottom: 2px solid var(--border-color);
            margin-top: 0;
        }

        .markdown-content h2 {
            font-size: 1.75rem;
            padding-bottom: 0.3em;
            border-bottom: 1px solid var(--border-color);
        }

        .markdown-content h3 { font-size: 1.5rem; }
        .markdown-content h4 { font-size: 1.25rem; }
        
        .markdown-content p {
            margin-bottom: 1.25em;
        }

        .markdown-content a {
            color: var(--primary);
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: border-color 0.2s;
        }

        .markdown-content a:hover {
            border-bottom-color: var(--primary);
        }

        /* Code Blocks */
        .markdown-content pre {
            background: #1e293b; /* Slate 800 */
            color: #e2e8f0;
            padding: 20px;
            border-radius: var(--radius-lg);
            overflow-x: auto;
            margin: 1.5em 0;
            font-family: var(--font-mono);
            font-size: 0.9rem;
            line-height: 1.5;
            box-shadow: var(--shadow-md);
        }

        .markdown-content code {
            background: var(--bg-body);
            color: var(--primary);
            padding: 0.2em 0.4em;
            border-radius: var(--radius-sm);
            font-family: var(--font-mono);
            font-size: 0.875em;
            border: 1px solid var(--border-color);
        }
        
        .markdown-content pre code {
            background: transparent;
            color: inherit;
            padding: 0;
            border: none;
        }

        /* Blockquotes */
        .markdown-content blockquote {
            border-left: 4px solid var(--primary);
            margin: 1.5em 0;
            padding: 1em 1.5em;
            color: var(--text-muted);
            background: var(--primary-light);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            font-style: italic;
        }

        /* Tables */
        .markdown-content table {
            border-collapse: separate;
            border-spacing: 0;
            width: 100%;
            margin: 1.5em 0;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            overflow: hidden;
        }

        .markdown-content th,
        .markdown-content td {
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }
        
        .markdown-content th {
            background-color: var(--bg-body);
            font-weight: 600;
            color: var(--text-main);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .markdown-content tr:last-child td {
            border-bottom: none;
        }
        
        .markdown-content tr:hover td {
            background-color: var(--bg-body);
        }

        /* Images */
        .markdown-content img {
            max-width: 100%;
            height: auto;
            border-radius: var(--radius-lg);
            margin: 1.5em 0;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
        }

        /* Lists */
        .markdown-content ul, 
        .markdown-content ol {
            margin: 1.25em 0;
            padding-left: 1.5em;
        }
        
        .markdown-content li {
            margin: 0.5em 0;
            padding-left: 0.5em;
        }
        
        .markdown-content li::marker {
            color: var(--text-light);
        }

        /* MathJax Enhancements */
        .markdown-content .math-inline {
            background-color: rgba(99, 102, 241, 0.1);
            padding: 2px 6px;
            border-radius: 4px;
            color: var(--primary);
        }

        .markdown-content .math-display {
            background-color: var(--bg-body);
            padding: 24px;
            border-radius: var(--radius-lg);
            margin: 2em 0;
            overflow-x: auto;
            border: 1px solid var(--border-color);
        }

        /* Welcome Page & Examples */
        .welcome-message {
            text-align: center;
            padding: 80px 20px;
            max-width: 700px;
            margin: 0 auto;
        }

        .welcome-message h2 {
            font-size: 2rem;
            color: var(--text-main);
            margin-bottom: 1.5rem;
        }
        
        .welcome-message p {
            color: var(--text-muted);
            font-size: 1.1rem;
            margin-bottom: 1rem;
        }

        .example-box {
            margin-top: 32px;
            padding: 24px;
            border-radius: var(--radius-lg);
            border: 1px solid var(--border-color);
            text-align: left;
            background: var(--bg-surface);
            box-shadow: var(--shadow-sm);
        }
        
        .example-box h3 {
            color: var(--text-main);
            font-size: 1.1rem;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .example-box.math {
            border-left: 4px solid var(--primary);
            background: linear-gradient(to right, rgba(99, 102, 241, 0.02), transparent);
        }
        
        .example-box.images {
            border-left: 4px solid #8b5cf6; /* Violet */
            background: linear-gradient(to right, rgba(139, 92, 246, 0.02), transparent);
        }

        /* Utility Classes */
        .toggle-header {
            position: fixed;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            background: var(--text-main);
            color: var(--bg-body);
            border: none;
            padding: 4px 12px;
            border-radius: 0 0 8px 8px;
            cursor: pointer;
            z-index: 100;
            font-size: 0.75rem;
            font-weight: 600;
            opacity: 0.8; /* Make it visible by default */
            transition: opacity 0.3s;
        }

        .toggle-header:hover {
            opacity: 1;
        }
        
        /* When header is hidden, maybe move the button or keep it? 
           It's fixed position, so it stays. */
        
        .back-button {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--bg-body);
            color: var(--text-muted);
            border: 1px solid var(--border-color);
            padding: 6px 12px;
            border-radius: var(--radius-sm);
            cursor: pointer;
            margin-bottom: 12px;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.2s;
            width: 100%;
            justify-content: center;
        }
        
        .back-button:hover {
            background: var(--bg-surface);
            color: var(--text-main);
            border-color: var(--border-hover);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .sidebar {
                position: absolute;
                height: 100%;
                box-shadow: var(--shadow-lg);
            }
            
            .sidebar.hidden {
                margin-left: -320px;
            }
            
            .markdown-wrapper {
                padding: 24px 16px 64px;
            }
            
            .header {
                padding: 12px 16px;
            }
        }
        
        /* Editor */
        .editor-container {
            display: none;
            width: 100%;
            min-height: 500px;
        }
        
        .editor-container.active {
            display: block;
        }
        
        .markdown-editor {
            width: 100%;
            min-height: 500px;
            padding: 20px;
            background: var(--bg-surface);
            color: var(--text-main);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            font-family: var(--font-mono);
            font-size: 1.0625rem; /* Match markdown-content */
            line-height: 1.75; /* Match markdown-content */
            resize: none;
            outline: none;
            overflow-y: hidden; /* Auto-resize */
        }
        
        .markdown-editor:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 2px var(--primary-light);
        }
'''