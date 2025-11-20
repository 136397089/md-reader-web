FROM python:3.12

# 设置工作目录
WORKDIR /app

# 安装 Python 包
RUN pip install --no-cache-dir \
    flask \
    markdown \
    cryptography \
    pillow -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制应用代码（如果有的话）
# COPY . .

# 暴露端口（Flask 默认端口）
EXPOSE 5000

# 启动命令（可根据需要修改）
CMD ["python", "-c", "print('Container is ready!')"]


