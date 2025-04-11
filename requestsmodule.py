import requests

response = requests.get("https://www.codewithharry.com")

print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'Nitesh',
    "body": 'Bhai',
    "userId": 12
    }

headers = {
    'Content-type': 'application/json; charset=UTF-8',
  }
    
response = requests.post(url,json=data,headers=headers)

print(response.text)