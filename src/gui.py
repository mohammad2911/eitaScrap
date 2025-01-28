import tkinter as tk
from tkinter import messagebox
from services.google_search import google_search, extract_links
from services.eitaa_scraper import extract_channel_ids
from utils.excel_writer import save_to_excel


def start_search(query):
    try:
        # جستجو در گوگل
        soup = google_search(query)
        links = extract_links(soup)

        # استخراج ایدی کانال‌ها
        channel_ids = extract_channel_ids(links)

        # ذخیره در اکسل
        save_to_excel(channel_ids)

        messagebox.showinfo("Success", f"Found {len(channel_ids)} channels. Saved to 'channel_ids.xlsx'.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def create_gui():
    # ایجاد پنجره اصلی
    window = tk.Tk()
    window.title("Eitaa Channel Scraper")
    window.geometry("400x200")

    # برچسب
    tk.Label(window, text="Enter a keyword to search:", font=("Arial", 12)).pack(pady=10)

    # جعبه متن
    query_entry = tk.Entry(window, width=30, font=("Arial", 12))
    query_entry.pack(pady=5)

    # دکمه جستجو
    search_button = tk.Button(
        window,
        text="Search",
        font=("Arial", 12),
        bg="#4CAF50",
        fg="white",
        command=lambda: start_search(query_entry.get())
    )
    search_button.pack(pady=20)

    # اجرای برنامه
    window.mainloop()


if __name__ == "__main__":
    create_gui()
