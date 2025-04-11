import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve the webpage.")
        return None

url = "https://www.example.com"
webpage_content = fetch_webpage(url)

if webpage_content:
    soup = BeautifulSoup(webpage_content, 'html.parser')
    # Add your code here to parse and process the web page content
    # For example, you could extract specific data or perform an API call
    
    print("Webpage content retrieved successfully:")
    print(soup.prettify())
