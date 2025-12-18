# JavaScript功能代码
# JavaScript功能代码
SCRIPTS = '''
        let currentPath = '';
        let currentFile = '';
        let sidebarVisible = true;
        let openTabs = []; // Array of { path, name }
        let activeTabPath = null;
        let isEditing = false;
        
        // Icons
        const ICONS = {
            folder: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
  <path d="M19.5 21a3 3 0 003-3v-4.5a3 3 0 00-3-3h-15a3 3 0 00-3 3V18a3 3 0 003 3h15zM1.5 10.146V6a3 3 0 013-3h5.379a2.25 2.25 0 011.59.659l2.122 2.121c.14.141.331.22.53.22H19.5a3 3 0 013 3v1.146A4.483 4.483 0 0019.5 9h-15a4.483 4.483 0 00-3 1.146z" />
</svg>`,
            markdown: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
  <path fill-rule="evenodd" d="M5.625 1.5H9a3.75 3.75 0 013.75 3.75v1.875c0 1.036.84 1.875 1.875 1.875H16.5a3.75 3.75 0 013.75 3.75v7.875c0 1.035-.84 1.875-1.875 1.875H5.625a1.875 1.875 0 01-1.875-1.875V3.375c0-1.036.84-1.875 1.875-1.875zM12.75 12a.75.75 0 00-1.5 0V15H7.875a.75.75 0 000 1.5H11.25v3a.75.75 0 001.5 0v-3h3.375a.75.75 0 000-1.5H12.75v-3z" clip-rule="evenodd" />
  <path d="M14.25 5.25a5.23 5.23 0 00-1.279-3.434 9.768 9.768 0 016.963 6.963A5.23 5.23 0 0016.5 7.5h-1.875a.375.375 0 01-.375-.375V5.25z" />
</svg>`,
            file: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
  <path fill-rule="evenodd" d="M5.625 1.5H9a3.75 3.75 0 013.75 3.75v1.875c0 1.036.84 1.875 1.875 1.875H16.5a3.75 3.75 0 013.75 3.75v7.875c0 1.035-.84 1.875-1.875 1.875H5.625a1.875 1.875 0 01-1.875-1.875V3.375c0-1.036.84-1.875 1.875-1.875zM12.75 12a.75.75 0 00-1.5 0V15H7.875a.75.75 0 000 1.5H11.25v3a.75.75 0 001.5 0v-3h3.375a.75.75 0 000-1.5H12.75v-3z" clip-rule="evenodd" />
  <path d="M14.25 5.25a5.23 5.23 0 00-1.279-3.434 9.768 9.768 0 016.963 6.963A5.23 5.23 0 0016.5 7.5h-1.875a.375.375 0 01-.375-.375V5.25z" />
</svg>`,
            arrowLeft: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
  <path fill-rule="evenodd" d="M7.72 12.53a.75.75 0 010-1.06l7.5-7.5a.75.75 0 111.06 1.06L9.31 12l6.97 6.97a.75.75 0 11-1.06 1.06l-7.5-7.5z" clip-rule="evenodd" />
</svg>`,
            arrowRight: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
  <path fill-rule="evenodd" d="M16.28 11.47a.75.75 0 010 1.06l-7.5 7.5a.75.75 0 01-1.06-1.06L14.69 12 7.72 5.03a.75.75 0 011.06-1.06l7.5 7.5z" clip-rule="evenodd" />
</svg>`,
            sun: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
  <path d="M12 2.25a.75.75 0 01.75.75v2.25a.75.75 0 01-1.5 0V3a.75.75 0 01.75-.75zM7.5 12a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM18.894 6.166a.75.75 0 00-1.06-1.06l-1.591 1.59a.75.75 0 101.06 1.061l1.591-1.59zM21.75 12a.75.75 0 01-.75.75h-2.25a.75.75 0 010-1.5H21a.75.75 0 01.75.75zM17.834 18.894a.75.75 0 001.06-1.06l-1.59-1.591a.75.75 0 10-1.061 1.06l1.59 1.591zM12 18a.75.75 0 01.75.75V21a.75.75 0 01-1.5 0v-2.25A.75.75 0 0112 18zM7.758 17.303a.75.75 0 00-1.061-1.06l-1.591 1.59a.75.75 0 001.06 1.061l1.591-1.59zM6 12a.75.75 0 01-.75.75H3a.75.75 0 010-1.5h2.25A.75.75 0 016 12zM6.697 7.757a.75.75 0 001.06-1.06l-1.59-1.591a.75.75 0 00-1.061 1.06l1.59 1.591z" />
</svg>`,
            moon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
  <path fill-rule="evenodd" d="M9.528 1.718a.75.75 0 01.162.819A8.97 8.97 0 009 6a9 9 0 009 9 8.97 8.97 0 003.463-.69.75.75 0 01.981.98 10.503 10.503 0 01-9.694 6.46c-5.799 0-10.5-4.7-10.5-10.5 0-4.368 2.667-8.112 6.46-9.694a.75.75 0 01.818.162z" clip-rule="evenodd" />
</svg>`,
            close: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 100%; height: 100%;">
  <path fill-rule="evenodd" d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z" clip-rule="evenodd" />
</svg>`
        };

        // Theme Management
        function initTheme() {
            const savedTheme = localStorage.getItem('theme');
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            
            if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
                document.documentElement.setAttribute('data-theme', 'dark');
            } else {
                document.documentElement.removeAttribute('data-theme');
            }
            updateThemeIcon();
        }

        function toggleTheme() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            if (currentTheme === 'dark') {
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem('theme', 'light');
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
            }
            updateThemeIcon();
        }

        function updateThemeIcon() {
            const themeToggle = document.getElementById('themeToggle');
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            themeToggle.innerHTML = isDark ? ICONS.sun : ICONS.moon;
        }

        // 页面加载时获取文件列表
        window.onload = function () {
            initTheme();
            loadFileList('');
        };

        // 退出登录
        function logout() {
            if (confirm(TRANSLATIONS['confirm_logout'])) {
                fetch('/api/logout', { method: 'POST' })
                    .then(() => {
                        window.location.href = '/login';
                    });
            }
        }

        // 切换侧边栏显示/隐藏
        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            const toggleIcon = document.getElementById('toggleIcon');

            sidebarVisible = !sidebarVisible;

            if (sidebarVisible) {
                sidebar.classList.remove('hidden');
                toggleIcon.innerHTML = ICONS.arrowLeft;
            } else {
                sidebar.classList.add('hidden');
                toggleIcon.innerHTML = ICONS.arrowRight;
            }
        }

        // 加载文件列表
        function loadFileList(path) {
            fetch(`/api/files?path=${encodeURIComponent(path)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('fileList').innerHTML =
                            `<li class="error">${TRANSLATIONS['load_error']}${data.error}</li>`;
                        return;
                    }

                    currentPath = data.current_path;
                    document.getElementById('currentPath').textContent =
                        `${TRANSLATIONS['current_path']}${currentPath || '/'}`;

                    const backButton = document.getElementById('backButton');
                    if (currentPath) {
                        backButton.style.display = 'inline-flex';
                        backButton.innerHTML = `${ICONS.arrowLeft} ${TRANSLATIONS['back_to_parent']}`;
                    } else {
                        backButton.style.display = 'none';
                    }

                    const fileList = document.getElementById('fileList');
                    fileList.innerHTML = '';

                    data.items.forEach(item => {
                        const li = document.createElement('li');
                        li.className = `file-item ${item.type}`;

                        li.dataset.path = item.path; // Store full path

                        if (item.type === 'folder') {
                            li.innerHTML = `${ICONS.folder} ${item.name}`;
                            li.onclick = () => loadFileList(item.path);
                        } else if (item.type === 'markdown') {
                            li.innerHTML = `${ICONS.markdown} ${item.name}`;
                            li.onclick = () => {
                                openFile(item.path, item.name);
                                // Sidebar update is handled in switchTab
                            };
                        } else {
                            li.innerHTML = `${ICONS.file} ${item.name}`;
                            li.style.color = 'var(--text-light)';
                        }

                        fileList.appendChild(li);
                    });

                    if (currentFile) {
                        const items = document.querySelectorAll('.file-item.markdown');
                        items.forEach(item => {
                            if (item.textContent.includes(currentFile.split('/').pop())) {
                                item.classList.add('active');
                            }
                        });
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('fileList').innerHTML =
                        `<li class="error">${TRANSLATIONS['load_file_list_error']}</li>`;
                });
        }

        // 返回上级目录
        function goBack() {
            const parentPath = currentPath.split('/').slice(0, -1).join('/');
            loadFileList(parentPath);
        }

        // Tab Management
        function openFile(path, name) {
            const existingTab = openTabs.find(t => t.path === path);
            
            if (existingTab) {
                switchTab(path);
            } else {
                // Create new tab
                const tab = { path, name };
                openTabs.push(tab);
                createTabElement(tab);
                createContentElement(tab);
                switchTab(path);
                loadMarkdownFile(path, document.getElementById(`tab-content-${CSS.escape(path)}`));
            }
        }

        function createTabElement(tab) {
            const tabBar = document.getElementById('tabBar');
            const tabEl = document.createElement('div');
            tabEl.className = 'tab';
            tabEl.id = `tab-${CSS.escape(tab.path)}`;
            tabEl.onclick = () => switchTab(tab.path);
            
            tabEl.innerHTML = `
                <span class="tab-icon">${ICONS.markdown}</span>
                <span class="tab-title" title="${tab.path}">${tab.name}</span>
                <span class="tab-close" onclick="closeTab('${CSS.escape(tab.path)}', event)">${ICONS.close}</span>
            `;
            
            tabBar.appendChild(tabEl);
        }

        function createContentElement(tab) {
            const wrapper = document.getElementById('markdownWrapper');
            const contentEl = document.createElement('div');
            contentEl.className = 'tab-content';
            contentEl.id = `tab-content-${CSS.escape(tab.path)}`;
            wrapper.appendChild(contentEl);
        }

        function switchTab(path) {
            activeTabPath = path;
            currentFile = path; // Update global currentFile

            // Update tabs UI
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            const activeTab = document.getElementById(`tab-${CSS.escape(path)}`);
            if (activeTab) activeTab.classList.add('active');

            // Update content visibility
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            const activeContent = document.getElementById(`tab-content-${CSS.escape(path)}`);
            if (activeContent) activeContent.classList.add('active');
            
            // Hide welcome message if a tab is open
            const welcomeTab = document.getElementById('welcome-tab');
            if (welcomeTab) {
                if (path) {
                    welcomeTab.classList.remove('active');
                } else {
                    welcomeTab.classList.add('active');
                }
            }

            // Update sidebar active state
            document.querySelectorAll('.file-item').forEach(el => el.classList.remove('active'));
            // Use CSS.escape for the selector because path might contain special chars
            // But CSS.escape escapes everything, so we need to be careful with quotes
            // Easier to iterate or use a simpler selector if possible.
            // Actually, querySelector with attribute value requires escaping quotes.
            // Let's just iterate to be safe and avoid complex escaping issues for now, 
            // or use the specific data attribute.
            const fileItems = document.querySelectorAll('.file-item.markdown');
            fileItems.forEach(item => {
                if (item.dataset.path === path) {
                    item.classList.add('active');
                }
            });
            
            // Reset edit mode when switching tabs
            isEditing = false;
            updateEditButtonState();
        }

        function closeTab(path, event) {
            if (event) event.stopPropagation();
            
            const index = openTabs.findIndex(t => t.path === path);
            if (index === -1) return;

            // Remove from array
            openTabs.splice(index, 1);

            // Remove DOM elements
            document.getElementById(`tab-${CSS.escape(path)}`).remove();
            document.getElementById(`tab-content-${CSS.escape(path)}`).remove();

            // Switch to another tab if closing active tab
            if (activeTabPath === path) {
                if (openTabs.length > 0) {
                    // Switch to the last opened tab or the one before/after
                    // Let's switch to the last one for simplicity, or the one at same index
                    const nextTab = openTabs[Math.min(index, openTabs.length - 1)];
                    switchTab(nextTab.path);
                } else {
                    activeTabPath = null;
                    currentFile = '';
                    // Show welcome tab
                    const welcomeTab = document.getElementById('welcome-tab');
                    if (welcomeTab) welcomeTab.classList.add('active');
                }
            }
        }

        // 加载Markdown文件
        function loadMarkdownFile(filePath, container) {
            if (!container) return;
            
            container.innerHTML =
                `<div class="loading">${TRANSLATIONS['loading']}</div>`;

            fetch(`/api/markdown?file=${encodeURIComponent(filePath)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        container.innerHTML =
                            `<div class="error">${TRANSLATIONS['load_error']}${data.error}</div>`;
                        return;
                    }

                    container.innerHTML = `
                        <div class="markdown-content" id="view-${CSS.escape(filePath)}">${data.html}</div>
                        <div class="editor-container" id="editor-${CSS.escape(filePath)}">
                            <textarea class="markdown-editor" spellcheck="false"></textarea>
                        </div>
                    `;
                    
                    // Set editor content
                    const textarea = container.querySelector('.markdown-editor');
                    if(textarea) {
                        textarea.value = data.raw_content || '';
                        // Auto resize on input
                        textarea.addEventListener('input', function() {
                            this.style.height = 'auto';
                            this.style.height = (this.scrollHeight) + 'px';
                        });
                    }
                    
                    // Update button state
                    if (activeTabPath === filePath) {
                        updateEditButtonState();
                    }

                    // 处理列表项样式
                    processListItems(container);

                    // 重新渲染MathJax
                    if (window.MathJax) {
                        MathJax.typesetPromise([container])
                            .then(() => {
                                console.log(TRANSLATIONS['mathjax_done']);
                                // 为数学公式添加样式类
                                addMathStyles(container);
                            })
                            .catch((err) => console.log(TRANSLATIONS['mathjax_error'], err));
                    }

                    // 处理图片加载错误
                    setupImageHandlers(container);
                })
                .catch(error => {
                    console.error('Error:', error);
                    container.innerHTML =
                        `<div class="error">${TRANSLATIONS['load_markdown_error']}</div>`;
                });
        }
        
        function setupImageHandlers(container) {
            const images = container.querySelectorAll('img');
            images.forEach(img => {
                img.onerror = function () {
                    this.style.border = '2px dashed #dc3545';
                    this.style.padding = '10px';
                    this.style.backgroundColor = '#f8d7da';
                    this.style.color = '#721c24';
                    this.title = TRANSLATIONS['image_load_error'] + this.src;
                };

                // 添加图片点击放大功能
                img.onclick = function () {
                    if (this.style.transform === 'scale(2)') {
                        this.style.transform = 'scale(1)';
                        this.style.cursor = 'zoom-in';
                        this.style.position = 'relative';
                        this.style.zIndex = '1';
                    } else {
                        this.style.transform = 'scale(2)';
                        this.style.cursor = 'zoom-out';
                        this.style.position = 'relative';
                        this.style.zIndex = '1000';
                    }
                };
            });
        }

        // 为数学公式添加样式类
        function addMathStyles(container) {
            const root = container || document;
            // 为行内数学公式添加样式
            const inlineMath = root.querySelectorAll('mjx-container[jax="CHTML"]:not([display="true"])');
            inlineMath.forEach(el => {
                if (!el.classList.contains('math-inline')) {
                    el.classList.add('math-inline');
                }
            });

            // 为块级数学公式添加样式
            const displayMath = root.querySelectorAll('mjx-container[jax="CHTML"][display="true"]');
            displayMath.forEach(el => {
                if (!el.parentElement.classList.contains('math-display')) {
                    const wrapper = document.createElement('div');
                    wrapper.classList.add('math-display');
                    el.parentNode.insertBefore(wrapper, el);
                    wrapper.appendChild(el);
                }
            });
        }

        // 处理列表项样式
        function processListItems(container) {
            const root = container || document;
            const content = root.querySelector('.markdown-content');
            if (!content) return;

            // 处理段落中的列表项
            const paragraphs = content.querySelectorAll('p');
            paragraphs.forEach(p => {
                const text = p.textContent.trim();
                // 检查是否以"- "或"  - "开头（支持缩进）
                const listMatch = text.match(/^(\s*)- (.+)/);
                if (listMatch) {
                    const indent = listMatch[1].length;
                    const listText = listMatch[2];

                    // 设置样式
                    p.setAttribute('data-list-item', 'true');
                    p.style.marginLeft = `${1.5 + indent * 0.5}em`;
                    p.style.textIndent = '-1.5em';
                    p.style.position = 'relative';

                    // 移除原始的"- "文本
                    p.innerHTML = p.innerHTML.replace(/^(\s*)- /, '');
                }
            });

            // 处理现有的ul li元素，确保嵌套缩进正确
            const lists = content.querySelectorAll('ul');
            lists.forEach(ul => {
                let level = 0;
                let parent = ul.parentElement;
                while (parent && parent !== content) {
                    if (parent.tagName === 'LI') {
                        level++;
                    }
                    parent = parent.parentElement;
                }

                // 根据嵌套级别调整缩进
                if (level > 0) {
                    ul.style.paddingLeft = `${1.5 + level * 0.5}em`;
                }
            });
        }

        // 在已有的script标签内添加
        let headerVisible = true;

        function toggleHeader() {
            const header = document.querySelector('.header');
            const toggleBtn = document.getElementById('toggleHeaderBtn');
            headerVisible = !headerVisible;

            if (headerVisible) {
                header.classList.remove('hidden');
                toggleBtn.textContent = TRANSLATIONS['hide_header'];
            } else {
                header.classList.add('hidden');
                toggleBtn.textContent = TRANSLATIONS['show_header'];
            }
        }

        // 添加键盘快捷键
        document.addEventListener('keydown', function (e) {
            // 原有的快捷键代码保持不变
            if ((e.ctrlKey || e.metaKey) && e.key === 'b') {
                e.preventDefault();
                toggleSidebar();
            }

            // 添加新的快捷键: Ctrl/Cmd + H 切换标题栏
            if ((e.ctrlKey || e.metaKey) && e.key === 'h') {
                e.preventDefault();
                toggleHeader();
            }
            
            // Save shortcut
            if ((e.ctrlKey || e.metaKey) && e.key === 's') {
                e.preventDefault();
                if (isEditing) {
                    saveFile();
                }
            }
        });

        function toggleEditMode() {
            if (!activeTabPath) return;
            
            const container = document.getElementById(`tab-content-${CSS.escape(activeTabPath)}`);
            if (!container) return;
            
            const viewEl = container.querySelector('.markdown-content');
            const editorEl = container.querySelector('.editor-container');
            const textarea = editorEl.querySelector('textarea');
            
            if (!isEditing) {
                // Switch to Edit Mode
                isEditing = true;
                viewEl.style.display = 'none';
                editorEl.classList.add('active');
                
                // Auto resize when entering edit mode
                textarea.style.height = 'auto';
                textarea.style.height = (textarea.scrollHeight) + 'px';
                
                textarea.focus();
                updateEditButtonState();
            } else {
                // Switch to Preview Mode (View Mode)
                const content = textarea.value;
                
                viewEl.innerHTML = `<div class="loading">${TRANSLATIONS['loading']}</div>`;
                viewEl.style.display = 'block';
                editorEl.classList.remove('active');
                
                fetch('/api/preview', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        content: content,
                        file_path: activeTabPath
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        viewEl.innerHTML = `<div class="error">${data.error}</div>`;
                    } else {
                        viewEl.innerHTML = data.html;
                        processListItems(container);
                        if (window.MathJax) {
                            MathJax.typesetPromise([viewEl]).then(() => addMathStyles(viewEl));
                        }
                        setupImageHandlers(viewEl);
                    }
                })
                .catch(err => {
                    viewEl.innerHTML = `<div class="error">${err}</div>`;
                });
                
                isEditing = false;
                updateEditButtonState();
            }
        }
        
        function saveFile() {
            if (!activeTabPath) return;
            
            const container = document.getElementById(`tab-content-${CSS.escape(activeTabPath)}`);
            if (!container) return;
            
            const textarea = container.querySelector('textarea');
            const content = textarea.value;
            
            fetch('/api/save', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    file: activeTabPath,
                    content: content
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(TRANSLATIONS['save_success']);
                } else {
                    alert(TRANSLATIONS['save_error'] + data.error);
                }
            })
            .catch(err => {
                alert(TRANSLATIONS['save_error'] + err);
            });
        }
        
        function updateEditButtonState() {
            const editBtn = document.getElementById('editBtn');
            const saveBtn = document.getElementById('saveBtn');
            
            if (!activeTabPath) {
                editBtn.style.display = 'none';
                saveBtn.style.display = 'none';
                return;
            }
            
            if (isEditing) {
                editBtn.style.display = 'flex';
                editBtn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
  <path d="M12 15a3 3 0 100-6 3 3 0 000 6z" />
  <path fill-rule="evenodd" d="M1.323 11.447C2.811 6.976 7.028 3.75 12.001 3.75c4.97 0 9.185 3.223 10.675 7.69.12.362.12.752 0 1.113-1.487 4.471-5.705 7.697-10.677 7.697-4.97 0-9.186-3.223-10.675-7.69a1.762 1.762 0 010-1.113zM17.25 12a5.25 5.25 0 11-10.5 0 5.25 5.25 0 0110.5 0z" clip-rule="evenodd" />
</svg>`;
                editBtn.title = TRANSLATIONS['preview'];
                saveBtn.style.display = 'flex';
            } else {
                editBtn.style.display = 'flex';
                editBtn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" style="width: 1.25rem; height: 1.25rem;">
                              <path d="M21.731 2.269a2.625 2.625 0 00-3.712 0l-1.157 1.157 3.712 3.712 1.157-1.157a2.625 2.625 0 000-3.712zM19.513 8.199l-3.712-3.712-12.15 12.15a5.25 5.25 0 00-1.32 2.214l-.8 2.685a.75.75 0 00.933.933l2.685-.8a5.25 5.25 0 002.214-1.32L19.513 8.2z" />
                            </svg>`;
                editBtn.title = TRANSLATIONS['edit'];
                saveBtn.style.display = 'none';
            }
        }

'''