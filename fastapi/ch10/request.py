import requests

url = 'http://127.0.0.1:8000/login'
data= {
    "username" : "park",
    "password" : "1234"
}

res = requests.post(url, json=data)

print(res)
print(res.text)