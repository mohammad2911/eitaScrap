import sys
from services.google_search import google_search_selenium
from services.eitaa_scraper import extract_channel_ids
from src.gui.main_window import start_app
from utils.excel_writer import save_to_excel

def cli_main(query):
    print(f"Searching for '{query}' on Google...")

    # جستجو در گوگل با استفاده از Selenium
    links = google_search_selenium(query)
    print(f"Found {len(links)} links.")

    # استخراج ایدی کانال‌ها
    channel_ids = extract_channel_ids(links)
    print(f"Extracted {len(channel_ids)} channel IDs.")

    # ذخیره در اکسل
    save_to_excel(channel_ids)
    print("Results saved to 'channel_ids.xlsx'.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # حالت CLI
        cli_main(sys.argv[1])
    else:
        # حالت GUI
        start_app()
