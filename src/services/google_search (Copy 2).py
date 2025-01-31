from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

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

    # افزودن تنظیمات اضافی برای کاهش احتمال تشخیص
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # تغییر User-Agent به صورت تصادفی
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    ]
    options.add_argument(f'user-agent={random.choice(user_agents)}')

    search_url = f"https://www.google.com/search?q={query}+site:eitaa.com"
    print(search_url)
    driver.get(search_url)
    links = []
    time.sleep(random.uniform(3, 5))  # افزایش زمان بین درخواست‌ها به صورت تصادفی

    a_tags = driver.find_elements(By.XPATH, "//a[contains(@href, 'eitaa.com')]")
    for a_tag in a_tags:
        print(a_tag)
        link = a_tag.get_attribute('href')
        print(link)
        links.append(link)

    driver.quit()
    return links
