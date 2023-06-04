## Language Chain Flask 应用

这是一个使用 Language Chain 库进行各种自然语言处理任务（如问答和向量解析）的 Flask 网络应用。该应用允许用户通过 Web 界面与 Language Chain 功能进行交互。
提供API给其他软件调用，提供向量数据库更新以及获取基于向量的问答系统得到的答案

### 依赖库
- Python 3.x
- Flask
- Langchain 库

### 安装

1. 克隆代码库：

   ```
   git clone https://github.com/Aomferni/vecDbLLMApp.git
   ```

2. 进入项目目录：

   ```
   cd vecDbLLMApp
   ```

3. 安装所需的依赖项：

   ```
   pip install -r requirements.txt
   ```

### 使用方法

1. 配置环境变量：

   - `OPENAI_API_KEY`：应用使用的 OpenAI API KEY。
   - `PROXY_API_KEY`：应用使用的 代理的 API KEY
   - `USE_PROXY_LLM`：如果要使用 Proxy LLM API，请将其设置为 `"true"`；如果要直接使用 OpenAI LLM，请将其设置为 `"false"`。

2. 启动 Flask 服务器：

   ```
   python app.py
   ```

3. 在 Web 浏览器中访问 `http://localhost:5000`，即可进入应用程序。

### 功能

Flask 应用程序提供以下端点：

- `/`：应用程序的主页。
- `/setOpenAIKey`：设置 OpenAI API 密钥。
- `/setProxyLLMKey`：设置 Proxy LLM API 密钥。
- `/updateVecDb`：上传 PDF 文件，将其解析为向量，并更新向量数据库。
- `/testLLM`：通过提问来测试语言模型。根据配置，可使用 OpenAI LLM 或 Proxy LLM API。
- `/getVecLLMAnswer`：使用提供的问题从向量数据库检索答案。

### 示例

以下是使用该应用程序的几个示例：

1. 设置 OpenAI API 密钥：

   发送一个带有 `api_key` 参数的 POST 请求到 `/setOpenAIKey`，其中包含你的 OpenAI API 密钥。

2. 设置 Proxy LLM API 密钥：

   发送一个带有 `api_key` 参数的 POST 请求到 `/setProxyLLMKey`，其中包含你的 Proxy LLM API 密钥。

3. 更新向量数据库：

   将一个 PDF 文件上传到 `/updateVecDb` 端点。上传的文件将被解析为向量，并存储在向量数据库中。

4. 测试语言模型：

   发送一个带有 `question` 参数的 POST 请求到 `/testLLM`。响应将是语言模型生成的答案。

5. 获取向量数据库答案：

   发送一个带有 `question` 参数的 POST 请求到 `/getVecLLMAnswer`。应用程序将查询向量数据库以获取匹配的答案。如果找到，则返回答案；否则，使用语言模型生成答案。

### 致谢

- Langchain 库提供了向量解析和问答功能的基础功能。
- Flask 提供了 Web 应用程序框架。
- OpenAI 提供了语言模型和 API 集成。

