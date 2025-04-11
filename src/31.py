import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return None

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extracting data from the HTML using Beautiful Soup
    # This is just an example and might need adjustments based on your specific needs
    results = [line.strip() for line in soup.select('div.example_class')]
    return results

url = "https://example.com"  # Replace with the actual URL of the page you want to scrape
html_content = fetch_html(url)
if html_content:
    print("HTML content retrieved successfully:")
    print(html_content)
else:
    print("Failed to retrieve HTML content.")
