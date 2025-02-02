import pandas as pd

def save_to_excel(channel_ids, links=[], filename="channel_ids.xlsx"):
    # فرض بر این است که تعداد لینک‌ها و ID ها برابر است
    data = {
        "ایدی": channel_ids,
        "لینک": links
    }

    # ایجاد DataFrame
    df = pd.DataFrame(data)

    # ذخیره داده‌ها در اکسل
    df.to_excel(filename, index=False)
