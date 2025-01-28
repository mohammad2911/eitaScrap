from awesometkinter.bidirender import add_bidi_support
import tkinter as tk
import arabic_reshaper
from bidi.algorithm import get_display



def reshape_text_for_rtl(text):
    """اصلاح متن فارسی برای نمایش راست‌به‌چپ"""
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)


def start_app():
    """اجرای رابط کاربری اصلی"""
    root = tk.Tk()
    root.title("برنامه تایپ فارسی")
    root.geometry("400x200")

    # برچسب برای نمایش متن
    lbl = tk.Label(root, font=("Tahoma", 14))
    lbl.pack(pady=10)

    # ورودی متن
    entry = tk.Entry(root, font=("Tahoma", 14))
    entry.pack(pady=20, padx=20)

    # افزودن پشتیبانی راست به چپ به ویجت‌ها
    add_bidi_support(lbl)
    add_bidi_support(entry)

    # دکمه ارسال متن
    def submit_text():
        print("متن ارسال شد:", entry.get())
        lbl.config(text=entry.get())

    # اصلاح متن فارسی
    reshaped_text = reshape_text_for_rtl("ارسال")

    # ساخت دکمه با متن راست‌به‌چپ
    submit_button = tk.Button(
        root,
        text=reshaped_text,
        command=submit_text,
        font=("Tahoma", 14)
    )
    submit_button.pack(pady=20)


    root.mainloop()
