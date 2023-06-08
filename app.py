import os
import requests
from flask import Flask, render_template, request
import pdfplumber
from langchain.vectorstores import FAISS

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI

app = Flask(__name__)

OPENAI_API_KEY = "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"  # 随便填的KEY
# 初始化 Proxy LLM API
PROXY_API_KEY = "wx-oDlmE5uJMetKOv2EIufMKufLjk6M_393bbc04282f2a5f004ab0aac5684bf1"
USE_PROXY_LLM = False  # 是否使用 Proxy LLM
# knowledge_base = None  # 定义knowledge_base为全局变量


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/knowledge_qa', methods=['GET', 'POST'])
def knowledge_qa():
    print(os.getenv('OPENAI_API_KEY'))
    if request.method == 'POST':
        pdf_file = request.files['pdf']
        if pdf_file:
            # 文件处理逻辑
            text = ""
            with pdfplumber.open(pdf_file) as pdf_reader:
                for page in pdf_reader.pages:
                    text += page.extract_text()

            # 文本分片
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=50,
                length_function=len
            )
            chunks = text_splitter.split_text(text)

            # 创建embeddings
            embeddings = OpenAIEmbeddings()
            knowledge_base = FAISS.from_texts(chunks, embeddings)

            # 将处理结果传递给模板
            return render_template('index.html', knowledge_base=knowledge_base)
        return "文件错误，请重新上传"


@app.route('/api/setOpenAIKey', methods=['POST'])
def set_openai_key():
    api_key = request.form.get('api_key')
    print("传入的key是：" + api_key)
    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
        return "API Key 已设置"
    else:
        return "未提供有效的 API Key"


@app.route('/api/setProxyLLMKey', methods=['POST'])
def set_proxy_llm_key():
    api_key = request.form.get('api_key')
    print("传入的key是：" + api_key)
    if api_key:
        global PROXY_API_KEY
        PROXY_API_KEY = request.form.get('api_key')
        return "Proxy LLM API 密钥已设置"
    else:
        return "未提供有效的 API Key"


# @app.route('/api/setRoute', methods=['POST'])
# def set_route():
#     print("I'm setingRoute")
#     route = request.form.get('route')
    
#     if route == "official":
#         USE_PROXY_LLM = False
#     else:
#         USE_PROXY_LLM = True

#     return response


@app.route('/api/testLLM', methods=['POST'])
def test_llm():
    # print(os.getenv('OPENAI_API_KEY'))
    question = request.form.get('question')
    print(question)
    if not question:
        return "请输入问题"

    if USE_PROXY_LLM:
        print("代理路线回复")
        response = proxy_llm(question)
    else:
        print("官方路线回复")
        response = openai_llm(question)

    return response


def openai_llm(question):
    if not OPENAI_API_KEY:
        return "请先设置 OpenAI API 密钥"

    llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = llm(question)
    return response


def proxy_llm(question):
    headers = {
        'Authorization': f'Bearer {PROXY_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": 1,
        "max_tokens": 256,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "model": "gpt-3.5-turbo"
    }

    response = requests.post(
        'https://proxy.aidashi.wiki/v1/chat/completions', headers=headers, json=data)
    return response.json()


@app.route('/api/getVecLLMAnswer', methods=['POST'])
def get_vector_llm_answer():
    question = request.form.get('question')
    if not question:
        return "请输入问题"

    if not OPENAI_API_KEY:
        return "请先设置OpenAI API密钥"

    docs = knowledge_base.similarity_search(question, 1)
    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=question)
    return response


if __name__ == '__main__':
    app.run(debug=True)
