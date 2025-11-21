# Secure Markdown Reader 🔐

A feature-rich, secure and reliable Markdown file browser and editor with LaTeX math formula support, image display, and encrypted authentication.

## ✨ Features

### 🔒 Security Features
- **HTTPS Encrypted Transmission** - Use SSL/TLS to encrypt all network communications
- **RSA-2048 Asymmetric Encryption** - Password transmission using RSA encryption for security
- **Path Traversal Protection** - Prevent directory traversal attacks, ensure filesystem security
- **Session Management** - Support session timeout and automatic logout
- **File Size Limits** - Prevent resource exhaustion from large files

### 📝 Markdown Functionality
- **Full Markdown Support** - Support standard Markdown syntax and extensions
- **LaTeX Math Formulas** - Support inline formulas `$E=mc^2$` and block formulas `$$\int_0^1 x^2 dx$$`
- **Code Highlighting** - Syntax highlighting for multiple programming languages
- **Tables and TOC** - Auto-generate tables and document table of contents
- **Real-time Editing** - Edit Markdown files online with real-time saving

### 🖼️ Image Support
- **Multi-format Support** - JPG, PNG, GIF, BMP, WebP, SVG, etc.
- **Relative Paths** - Support relative path image references
- **Security Checks** - Automatically verify image path security
- **Interactive Viewing** - Click images to zoom in/out

### 🛠️ Technical Features
- **Python Flask** - Lightweight web framework
- **Docker Support** - Containerized deployment
- **Multi-threading** - Support concurrent access
- **Exception Handling** - Comprehensive error handling mechanism

## 🚀 Quick Start

### Method 1: Direct Execution

#### Requirements
- Python 3.11+
- pip package manager

#### Install Dependencies
```bash
# Clone the project
git clone <project-url>
cd markdown_reader

# Install dependencies
pip install flask markdown cryptography pillow
# Or use Tsinghua mirror
pip install flask markdown cryptography pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### Start Service
```bash
python markdown_reader.py

# Or specify target folder
python markdown_reader.py --target_folder /path/to/your/markdown/files
```

### Method 2: Docker Deployment

#### Build and Run
```bash
# Build Docker image
docker build -t markdown_reader .

# Run container
docker run -p 6100:5000 -v $(pwd)/..:/app markdown_reader
```

#### Using Docker Compose
```bash
# Start service
docker compose up -d

# View logs
docker compose logs -f

# Stop service
docker compose down
```

## 🎯 Usage

1. **Start Service**
   - Direct run: visit `https://localhost:5000`
   - Docker: visit `https://localhost:6100`

2. **Login System**
   - Default password: `grant91`
   - Password will be transmitted using RSA encryption

3. **Browse Files**
   - Select Markdown files from the file list
   - Support directory navigation and file search

4. **View Content**
   - Auto-render Markdown format
   - Support LaTeX math formula display
   - Auto-load and display images

5. **Edit Files**
   - Click edit button to modify content
   - Auto-create backup files
   - Real-time save changes

## 📐 Math Formula Syntax

### Inline Formulas
Mass-energy equation: $E = mc^2$

### Block Formulas
Integral formula:
$$\int_0^1 x^2 dx = \frac{1}{3}$$

### Matrix Example
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

## 🖼️ Image Usage

### Supported Formats
- JPG/JPEG
- PNG
- GIF
- BMP
- WebP
- SVG
- ICO

### Reference Method
```markdown
![Image description](./images/example.jpg)
```

## ⚙️ Configuration Options

### Server Configuration
- **Port**: 5000 (modifiable)
- **SSL**: Auto-generate self-signed certificates
- **Session timeout**: 10000 seconds
- **Max file size**: 50MB
- **Target Folder**: Specify via `--target_folder` at startup

### Security Configuration
- **Password**: Can be modified in code `stored_password`
- **RSA Keys**: Auto-generated on each startup
- **Path checking**: Auto-verify file path security

## 🔧 Project Structure

```
markdown_reader/
├── markdown_reader.py      # Main program file
├── template/              # Template files
│   ├── main_template.py   # Main page template
│   ├── login_template.py  # Login page template
│   ├── styles.py          # CSS styles
│   └── scripts.py         # JavaScript scripts
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile            # Docker image configuration
├── pyproject.toml        # Python project configuration
├── run.sh               # Startup script
├── server.crt           # SSL certificate (auto-generated)
├── server.key           # SSL private key (auto-generated)
└── .backups/            # Backup folder (auto-created)
```

## ⚠️ Important Notes

1. **SSL Certificate**: Uses self-signed certificates, browsers will show security warnings, choose "Continue to site"
2. **Password Security**: Recommend changing default password and regular updates
3. **File Permissions**: Ensure Python has read/write permissions for files
4. **Port Usage**: Ensure port 5000 (or custom port) is not occupied by other programs
5. **Network Access**: 0.0.0.0 binding allows external access, pay attention to security

## 🤝 Contributing

1. Fork the project
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📄 License

This project is licensed under an open source license, see LICENSE file for details.

## 📞 Support

If you encounter issues or need help:
1. Check project documentation
2. Submit an Issue
3. Email the developer

---

**Enjoy the secure and convenient Markdown reading experience!** 📚✨