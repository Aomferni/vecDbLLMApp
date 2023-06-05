import requests

url = 'https://proxy.aidashi.wiki/v1/chat/completions'
headers = {
    'Authorization': 'Bearer wx-oDlmE5uJMetKOv2EIufMKufLjk6M_26656f7f11df12026d577ce7572e4830',
    'Content-Type': 'application/json'
}
data = {
    "messages": [
        {
            "role": "user",
            "content": "请作为一个长者，对我这个技术小白说一些鼓励的话语"
        }
    ],
    "temperature": 1,
    "max_tokens": 256,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "model": "gpt-3.5-turbo"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
