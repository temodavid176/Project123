import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed with status {response.status_code}")

url = "https://api.example.com/data"
data = fetch_data(url)
print(data)
