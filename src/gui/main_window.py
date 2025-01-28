import tkinter as tk
from awesometkinter.bidirender import add_bidi_support
from services.google_search import google_search_selenium  # تغییر این خط
from services.eitaa_scraper import extract_channel_ids
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
        query = entry.get()
        result_label.config(text="در حال جستجو...")

        # جستجو در گوگل و استخراج لینک‌ها با استفاده از selenium
        links = google_search_selenium(query)  # استفاده از تابع google_search_selenium

        # استخراج آیدی کانال‌ها
        channel_ids = extract_channel_ids(links)

        # ذخیره در اکسل
        save_to_excel(channel_ids)

        # نمایش نتیجه
        result_label.config(text=f"تعداد کانال‌های پیدا شده: {len(channel_ids)}\n"
                                 f"لینک‌ها در 'channel_ids.xlsx' ذخیره شدند.")

    # دکمه جستجو
    search_button = tk.Button(root, text="جستجو", font=("Tahoma", 14), command=search_action)
    search_button.pack(pady=20)

    root.mainloop()
