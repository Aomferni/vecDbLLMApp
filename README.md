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

### 在 Railway 上部署

[Railway](https://railway.app/) 是一个可以简化应用程序部署和托管的平台。以下是使用 Railway 部署 Language Chain 应用程序的步骤：

1. 创建 Railway 帐户并登录。

2. 在你的项目中创建一个新的应用程序。

3. 设置项目的环境变量：
   - `OPENAI_API_KEY`：将你的 OpenAI API 密钥设置为该变量的值。
   - `USE_PROXY_LLM`：如果要使用 Proxy LLM API，请将其设置为 `"true"`；如果要直接使用 OpenAI LLM，请将其设置为 `"false"`。

4. 在项目设置中，将 `command` 设置为 `python app.py`，将 `port` 设置为 `5000`。

5. 在项目根目录中创建一个名为 `railway.yml` 的文件，并将以下内容添加到文件中：

   ```yaml
   envs:
     - OPENAI_API_KEY
     - USE_PROXY_LLM
   ```

6. 将项目部署到 Railway 上。Railway 将自动构建和部署应用程序。

7. 部署完成后，你将获得一个分配的 URL，即可访问部署的应用程序。

### 在 CodeSandbox 上部署

[CodeSandbox](https://codesandbox.io/) 是一个在线代码编辑和部署平台，可以帮助你轻松地将应用程序部署到云端。以下是使用 CodeSandbox 部署 Language Chain 应用程序的步骤：

1. 访问 CodeSandbox 网站并登录。

2. 创建一个新的沙箱。

3. 将应用程序代码复制粘贴到 CodeSandbox 的编辑器中。

4. 在编辑器中创建一个名为 `.env` 的文件，并添加以下内容：

   ```
   OPENAI_API_KEY=YOUR_OPENAI_API_KEY
   USE_PROXY_LLM=false
   ```

   将 `YOUR_OPENAI_API_KEY` 替换为你的 OpenAI API 密钥。

5. 在编辑器中，点击运行按钮以启动应用程序。

6. 运行完成后，你将获得一个分配的 URL，即可访问部署的应用程序。

### 致谢

- Langchain 库提供了向量解析和问答功能的基础功能。
- Flask 提供了 Web 应用程序框架。
- OpenAI 提供了语言模型和 API 集成。
