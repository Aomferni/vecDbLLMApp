import requests

url = 'http://localhost:5000/testLLM'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'question': '请作为一个软件技术专家，给新手一点建议'}

response = requests.post(url, headers=headers, data=data)
if response.status_code == 200:
    print(response.text)
else:
    print('请求失败:', response.status_code)
