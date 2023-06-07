import requests

class TestSuite:
    def __init__(self):
        self.proxy_api_key = ""
        self.openai_api_key = ""

    def run_test_proxy_api(self, question):
        url = 'http://localhost:5000/api/testLLM'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'question': question}

        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print(response.text)
        else:
            print('请求失败:', response.status_code)

    def run_test_set_openai_key(self, openai_api_key):
        url = 'http://localhost:5000/api/setOpenAIKey'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'api_key': openai_api_key}

        response = requests.post(url, headers=headers, data=data)
        print(response.text)
    
    def run_test_set_proxy_api_key(self, proxy_api_key):
        url = 'http://localhost:5000/api/setProxyLLMKey'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'api_key': proxy_api_key}

        response = requests.post(url, headers=headers, data=data)
        print(response.text)

    def run_selected_test(self):
        while True:
            print("请选择要运行的测试接口:")
            print("1. 测试 Proxy API")
            print("2. 设置 OpenAI 密钥")
            print("3. 设置 Proxy LLM 密钥")
            print("输入 'quit' 退出")

            choice = input("输入选择编号: ")

            if choice == "1":
                question = input("输入问题: ")
                self.run_test_proxy_api(question)
            elif choice == "2":
                openai_api_key = input("输入 OpenAI 密钥: ")
                self.run_test_set_openai_key(openai_api_key)
            elif choice == "3":
                proxy_api_key = input("输入 Proxy LLM 密钥: ")
                self.run_test_set_proxy_api_key(proxy_api_key)
            elif choice.lower() == "quit":
                break
            else:
                print("无效的选择")


if __name__ == '__main__':
    test_suite = TestSuite()

    # 设置 API 密钥
    test_suite.openai_api_key = "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"
    test_suite.proxy_api_key = "wx-oDlmE5uJMetKOv2EIufMKufLjk6M_26656f7f11df12026d577ce7572e4830"

    # 运行用户选择的测试接口
    test_suite.run_selected_test()
