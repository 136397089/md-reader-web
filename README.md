# 安全Markdown阅读器 🔐

一个功能丰富、安全可靠的Markdown文件浏览和编辑器，支持LaTeX数学公式、图片显示和加密认证。

## ✨ 特性

### 🔒 安全特性
- **HTTPS加密传输** - 使用SSL/TLS加密所有网络通信
- **RSA-2048非对称加密** - 密码采用RSA加密传输，确保安全性
- **路径遍历保护** - 防止目录遍历攻击，确保文件系统安全
- **会话管理** - 支持会话超时和自动登出
- **文件大小限制** - 防止大文件导致的资源耗尽

### 📝 Markdown功能
- **完整Markdown支持** - 支持标准Markdown语法和扩展
- **LaTeX数学公式** - 支持行内公式 `$E=mc^2$` 和块级公式 `$$\int_0^1 x^2 dx$$`
- **代码高亮** - 支持多种编程语言的语法高亮
- **表格和目录** - 自动生成表格和文档目录
- **实时编辑** - 在线编辑Markdown文件并实时保存

### 🖼️ 图片支持
- **多格式支持** - JPG、PNG、GIF、BMP、WebP、SVG等
- **相对路径** - 支持相对路径图片引用
- **安全检查** - 自动验证图片路径安全性
- **交互式查看** - 点击图片可放大/缩小

### 🛠️ 技术特性
- **Python Flask** - 轻量级Web框架
- **Docker支持** - 容器化部署
- **多线程** - 支持并发访问
- **异常处理** - 完善的错误处理机制

## 🚀 快速开始

### 方式一：直接运行

#### 环境要求
- Python 3.11+
- pip包管理器

#### 安装依赖
```bash
# 克隆项目
git clone <项目地址>
cd markdown_reader

# 安装依赖
pip install flask markdown cryptography pillow
# 或使用清华镜像源
pip install flask markdown cryptography pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 启动服务
```bash
python markdown_reader.py
```

### 方式二：Docker部署

#### 构建并运行
```bash
# 构建Docker镜像
docker build -t markdown_reader .

# 运行容器
docker run -p 6100:5000 -v $(pwd)/..:/app markdown_reader
```

#### 使用Docker Compose
```bash
# 启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

## 🎯 使用方法

1. **启动服务**
   - 直接运行：访问 `https://localhost:5000`
   - Docker：访问 `https://localhost:6100`

2. **登录系统**
   - 默认密码：`grant91`
   - 密码将使用RSA加密传输

3. **浏览文件**
   - 在文件列表中选择Markdown文件
   - 支持目录导航和文件搜索

4. **查看内容**
   - 自动渲染Markdown格式
   - 支持LaTeX数学公式显示
   - 图片自动加载和显示

5. **编辑文件**
   - 点击编辑按钮修改内容
   - 自动创建备份文件
   - 实时保存更改

## 📐 数学公式语法

### 行内公式
质能方程：$E = mc^2$

### 块级公式
积分公式：
$$\int_0^1 x^2 dx = \frac{1}{3}$$

### 矩阵示例
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

## 🖼️ 图片使用

### 支持的格式
- JPG/JPEG
- PNG
- GIF
- BMP
- WebP
- SVG
- ICO

### 引用方式
```markdown
![图片描述](./images/example.jpg)
```

## ⚙️ 配置选项

### 服务器配置
- **端口**：5000（可修改）
- **SSL**：自动生成自签名证书
- **会话超时**：10000秒
- **最大文件大小**：50MB

### 安全配置
- **密码**：可在代码中修改 `stored_password`
- **RSA密钥**：每次启动自动生成
- **路径检查**：自动验证文件路径安全性

## 🔧 项目结构

```
markdown_reader/
├── markdown_reader.py      # 主程序文件
├── template/              # 模板文件
│   ├── main_template.py   # 主页面模板
│   ├── login_template.py  # 登录页面模板
│   ├── styles.py          # CSS样式
│   └── scripts.py         # JavaScript脚本
├── docker-compose.yml     # Docker Compose配置
├── Dockerfile            # Docker镜像配置
├── pyproject.toml        # Python项目配置
├── run.sh               # 启动脚本
├── server.crt           # SSL证书（自动生成）
├── server.key           # SSL私钥（自动生成）
└── .backups/            # 备份文件夹（自动创建）
```

## ⚠️ 注意事项

1. **SSL证书**：使用自签名证书，浏览器会显示安全警告，选择"继续访问"即可
2. **密码安全**：建议修改默认密码并定期更换
3. **文件权限**：确保Python有读写文件的权限
4. **端口占用**：确保5000端口（或自定义端口）未被其他程序占用
5. **网络访问**：0.0.0.0绑定允许外部访问，注意安全性

## 🤝 贡献

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/新功能`)
3. 提交更改 (`git commit -am '添加新功能'`)
4. 推送分支 (`git push origin feature/新功能`)
5. 创建Pull Request

## 📄 许可证

本项目采用开源许可证，详见LICENSE文件。

## 📞 支持

如果遇到问题或需要帮助：
1. 查看项目文档
2. 提交Issue
3. 发送邮件联系开发者

---

**享受安全便捷的Markdown阅读体验！** 📚✨