import tkinter as tk
from awesometkinter.bidirender import add_bidi_support
from services.google_search_api import google_search_api
from services.eitaa_scraper import extract_eitaa_ids
from utils.excel_writer import save_to_excel

def start_app():
    """اجرای رابط گرافیکی"""
    root = tk.Tk()
    root.title("برنامه جستجوی کانال‌های ایتا")
    root.geometry("400x300")

    # ورودی جستجو
    entry = tk.Entry(root, font=("Tahoma", 14), justify="right")
    add_bidi_support(entry)
    entry.pack(pady=20, padx=20)

    # برچسب نتیجه
    result_label = tk.Label(root, font=("Tahoma", 12), wraplength=350, justify="left")
    add_bidi_support(result_label)
    result_label.pack(pady=10)

    # تابع برای جستجو
    def search_action():
        query = entry.get() + " site:eitaa.com"
        result_label.config(text="در حال جستجو...")

        api_key = "AIzaSyBM4_VSs1zQUNiFr26YaLKJrn_ae-xdISo"  # API Key خود را اینجا وارد کنید
        cse_id = "36f9b1acc1d9c41b0"  # Custom Search Engine ID خود را اینجا وارد کنید


        links = google_search_api(query, api_key, cse_id,500)

        # استخراج آیدی کانال‌ها
        channel_ids = extract_eitaa_ids(links)

        # ذخیره در اکسل
        save_to_excel(channel_ids,links)

        # نمایش نتیجه
        result_label.config(text=f"found: {len(channel_ids)}\n")

    # دکمه جستجو
    search_button = tk.Button(root, text="search", font=("Tahoma", 14), command=search_action)
    search_button.pack(pady=20)

    root.mainloop()
