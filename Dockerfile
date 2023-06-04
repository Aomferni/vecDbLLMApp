# 使用Python 3.8 作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的/app目录下
COPY . /app

# 安装所需的依赖库
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用程序使用的端口
EXPOSE 5000

# 运行应用程序
CMD [ "python", "app.py" ]
