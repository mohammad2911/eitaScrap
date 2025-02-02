import sys
from services.google_search_api import google_search_api
from services.eitaa_scraper import extract_eitaa_ids
from src.gui.main_window import start_app
from utils.excel_writer import save_to_excel

def cli_main(query, api_key, cse_id):
    print(f"Searching for '{query}' on Google...")

    # جستجو در گوگل با استفاده از API گوگل
    links = google_search_api(query, api_key, cse_id)
    print(f"Found {len(links)} links.")

    # استخراج ایدی کانال‌ها
    channel_ids = extract_eitaa_ids(links)
    print(f"Extracted {len(channel_ids)} channel IDs.")

    # ذخیره در اکسل
    save_to_excel(channel_ids)
    print("Results saved to 'channel_ids.xlsx'.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # حالت CLI
        api_key = "YOUR_API_KEY"  # API Key خود را اینجا وارد کنید
        cse_id = "YOUR_CSE_ID"  # Custom Search Engine ID خود را اینجا وارد کنید
        cli_main(sys.argv[1], api_key, cse_id)
    else:
        # حالت GUI
        start_app()
