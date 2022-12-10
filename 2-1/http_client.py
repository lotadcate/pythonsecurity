import requests

url = "https://localhost:8000"
response = requests.get(url)
print(response.text)
