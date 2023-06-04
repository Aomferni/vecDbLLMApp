# vecDbLLMApp
提供API给其他软件调用，提供向量数据库更新以及获取基于向量的问答系统得到的答案

## 安装

1. Clone the repository: git clone https://github.com/Aomferni/vecDbLLMApp.git
2. Navigate to the project directory:
3. Install the required dependencies: pip install -r requirements.txt

配置
在运行应用程序之前，您需要配置API密钥和设置。打开 app.py 文件并更新以下变量：

OPENAI_API_KEY：设置您的OpenAI API密钥。
USE_PROXY_LLM：如果要使用Proxy LLM API，请设置为 True，或者设置为 False 使用OpenAI API。

使用方法
启动应用程序：python app.py
打开Web浏览器，访问 http://localhost:5000 来访问Web界面。

通过点击“设置OpenAI API密钥”按钮并输入您的API密钥来设置OpenAI API密钥。

通过上传包含要查询的文档的PDF文件来更新向量数据库。点击“更新向量数据库”按钮并选择一个PDF文件。

现在，您可以使用LLM API提问并获取答案。在输入字段中输入您的问题，然后点击“提问”按钮。应用程序将根据问题使用配置的LLM API提供答案。
