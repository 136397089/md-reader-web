# JavaScript功能代码
SCRIPTS = '''
        let currentPath = '';
        let currentFile = '';
        let sidebarVisible = true;

        // 页面加载时获取文件列表
        window.onload = function () {
            loadFileList('');
        };

        // 退出登录
        function logout() {
            if (confirm('确定要退出登录吗？')) {
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
                toggleIcon.textContent = '◀';
            } else {
                sidebar.classList.add('hidden');
                toggleIcon.textContent = '▶';
            }
        }

        // 加载文件列表
        function loadFileList(path) {
            fetch(`/api/files?path=${encodeURIComponent(path)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('fileList').innerHTML =
                            `<li class="error">错误: ${data.error}</li>`;
                        return;
                    }

                    currentPath = data.current_path;
                    document.getElementById('currentPath').textContent =
                        `当前路径: ${currentPath || '/'}`;

                    const backButton = document.getElementById('backButton');
                    if (currentPath) {
                        backButton.style.display = 'inline-block';
                    } else {
                        backButton.style.display = 'none';
                    }

                    const fileList = document.getElementById('fileList');
                    fileList.innerHTML = '';

                    data.items.forEach(item => {
                        const li = document.createElement('li');
                        li.className = `file-item ${item.type}`;

                        if (item.type === 'folder') {
                            li.innerHTML = `📁 ${item.name}`;
                            li.onclick = () => loadFileList(item.path);
                        } else if (item.type === 'markdown') {
                            li.innerHTML = `📄 ${item.name}`;
                            li.onclick = () => {
                                loadMarkdownFile(item.path);
                                document.querySelectorAll('.file-item').forEach(el =>
                                    el.classList.remove('active'));
                                li.classList.add('active');
                                currentFile = item.path;
                            };
                        } else {
                            li.innerHTML = `📄 ${item.name}`;
                            li.style.color = '#999';
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
                        '<li class="error">加载文件列表失败</li>';
                });
        }

        // 返回上级目录
        function goBack() {
            const parentPath = currentPath.split('/').slice(0, -1).join('/');
            loadFileList(parentPath);
        }

        // 加载Markdown文件
        function loadMarkdownFile(filePath) {
            document.getElementById('markdownContent').innerHTML =
                '<div class="loading">正在加载...</div>';

            fetch(`/api/markdown?file=${encodeURIComponent(filePath)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('markdownContent').innerHTML =
                            `<div class="error">错误: ${data.error}</div>`;
                        return;
                    }

                    document.getElementById('markdownContent').innerHTML =
                        `<div class="markdown-content">${data.html}</div>`;

                    // 处理列表项样式
                    processListItems();

                    // 重新渲染MathJax
                    if (window.MathJax) {
                        MathJax.typesetPromise([document.getElementById('markdownContent')])
                            .then(() => {
                                console.log('MathJax渲染完成');
                                // 为数学公式添加样式类
                                addMathStyles();
                            })
                            .catch((err) => console.log('MathJax渲染错误:', err));
                    }

                    // 处理图片加载错误
                    const images = document.querySelectorAll('#markdownContent img');
                    images.forEach(img => {
                        img.onerror = function () {
                            this.style.border = '2px dashed #dc3545';
                            this.style.padding = '10px';
                            this.style.backgroundColor = '#f8d7da';
                            this.style.color = '#721c24';
                            this.title = '图片加载失败: ' + this.src;
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
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('markdownContent').innerHTML =
                        '<div class="error">加载Markdown文件失败</div>';
                });
        }

        // 为数学公式添加样式类
        function addMathStyles() {
            // 为行内数学公式添加样式
            const inlineMath = document.querySelectorAll('mjx-container[jax="CHTML"]:not([display="true"])');
            inlineMath.forEach(el => {
                if (!el.classList.contains('math-inline')) {
                    el.classList.add('math-inline');
                }
            });

            // 为块级数学公式添加样式
            const displayMath = document.querySelectorAll('mjx-container[jax="CHTML"][display="true"]');
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
        function processListItems() {
            const content = document.querySelector('.markdown-content');
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
                toggleBtn.textContent = '隐藏标题栏';
            } else {
                header.classList.add('hidden');
                toggleBtn.textContent = '显示标题栏';
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
        });

'''