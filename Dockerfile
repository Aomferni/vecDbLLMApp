# 使用 Python 3.9 作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制应用代码到容器中
COPY . .

# 安装依赖库
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用的端口号
EXPOSE 5000

# 启动应用
CMD ["python", "app.py"]
