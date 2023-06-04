# vecDbLLMApp
提供API给其他软件调用，提供向量数据库更新以及获取基于向量的问答系统得到的答案

## 安装

1. Clone the repository: git clone https://github.com/Aomferni/vecDbLLMApp.git
2. Navigate to the project directory:
3. Install the required dependencies: pip install -r requirements.txt

## 配置
在运行应用程序之前，您需要配置API密钥和设置。打开 app.py 文件并更新以下变量：

OPENAI_API_KEY：设置您的OpenAI API密钥。
USE_PROXY_LLM：如果要使用Proxy LLM API，请设置为 True，或者设置为 False 使用OpenAI API。

## 使用方法
启动应用程序：python app.py
打开Web浏览器，访问 http://localhost:5000 来访问Web界面。

通过 /setOpenAIKey API 设置OpenAI API密钥。

通过 /updateVecDb API 上传包含要查询的文档的PDF文件来更新向量数据库。

通过 /testLLM API 来进行直接的提问和获取答案。

通过 /getVecLLMAnswer API 获取基于 Langchain 的向量匹配系统的回答
