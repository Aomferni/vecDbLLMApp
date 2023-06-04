import os
import json
import requests
from flask import Flask, render_template, request

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain import VectorDBQA

app = Flask(__name__)

OPENAI_API_KEY = ""  # 初始化OpenAI API密钥为空
VECTOR_DB = Chroma()  # 初始化向量数据库
PROXY_API_KEY = "wx-oDlmE5uJMetKOv2EIufMKufLjk6M_393bbc04282f2a5f004ab0aac5684bf1"  # 初始化 Proxy LLM API
USE_PROXY_LLM = os.environ.get("USE_PROXY_LLM", "false").lower() == "true"  # 是否使用 Proxy LLM

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/setOpenAIKey', methods=['POST'])
def set_openai_key():
    global OPENAI_API_KEY
    OPENAI_API_KEY = request.form.get('api_key')
    return "OpenAI API密钥已设置"

@app.route('/setProxyLLMKey', methods=['POST'])
def set_proxy_llm_key():
    global PROXY_API_KEY
    PROXY_API_KEY = request.form.get('api_key')
    return "Proxy LLM API 密钥已设置"

@app.route('/updateVecDb', methods=['POST'])
def update_vector_db():
    file = request.files['file']
    if file and file.filename.endswith('.pdf'):
        # 处理上传的PDF文件，进行向量解析并存入向量数据库
        # 假设这里使用的是langchain库中的相应功能进行向量解析和存储
        vectors = parse_pdf_to_vectors(file)
        VECTOR_DB.update(vectors)
        return "向量数据库已更新"
    else:
        return "请上传PDF文件"

@app.route('/testLLM', methods=['POST'])
def test_llm():
    question = request.form.get('question')
    if not question:
        return "请输入问题"
        
    if USE_PROXY_LLM:
        response = proxy_llm(question)
    else:
        response = openai_llm(question)
    
    return response

def openai_llm(question):
    if not OPENAI_API_KEY:
        return "请先设置 OpenAI API 密钥"
    
    llm = OpenAI(api_key=OPENAI_API_KEY)
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
    
    response = requests.post('https://proxy.aidashi.wiki/v1/chat/completions', headers=headers, json=data)
    return response.json()

@app.route('/getVecLLMAnswer', methods=['POST'])
def get_vector_llm_answer():
    question = request.form.get('question')
    if not question:
        return "请输入问题"
    
    # 使用向量数据库和OpenAI模型进行问答
    answer = VECTOR_DB.query(question)
    if answer:
        return answer
    
    if not OPENAI_API_KEY:
        return "请先设置OpenAI API密钥"
    
    response = generate_answer(question)
    return response

def generate_answer(question):
    llm = OpenAI(model_name="gpt-3.5-turbo", max_tokens=512, temperature=0)
    chain = VectorDBQA.from_chain_type(llm=llm, chain_type="stuff", vectorstore=VECTOR_DB, return_source_documents=True)
    answer = chain.ask(question)
    return answer

def parse_pdf_to_vectors(file):
    # 使用OpenAIEmbeddings对PDF文件进行向量解析
    embeddings = OpenAIEmbeddings()
    vectors = embeddings.parse_pdf(file)
    return vectors

if __name__ == '__main__':
    app.run(debug=True)
