import requests

url = 'http://localhost:5000/api/setOpenAIKey'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'api_key': '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'}

response = requests.post(url, headers=headers, data=data)
print(response.text)
