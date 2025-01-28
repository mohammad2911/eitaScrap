import requests
from bs4 import BeautifulSoup

def google_search(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    search_url = f"https://www.google.com/search?q={query}+site:eitaa.com"
    print(search_url)
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    return soup

def extract_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        print(link)
        if 'eitaa.com' in link:  # فقط لینک‌های مربوط به ایتا
            links.append(link)
    return links
