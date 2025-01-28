from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def google_search_selenium(query):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("window-size=1200x600")
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    search_url = f"https://www.google.com/search?q={query}+site:eitaa.com"
    print(search_url)
    driver.get(search_url)
    links = []
    time.sleep(3)
    print(driver)
    a_tags = driver.find_elements(By.XPATH, "//a[contains(@href, 'eitaa.com')]")
    for a_tag in a_tags:
        link = a_tag.get_attribute('href')
        links.append(link)

    driver.quit()
    return links
