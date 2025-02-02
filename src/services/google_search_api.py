from googleapiclient.discovery import build


def google_search_api(query, api_key, cse_id,num_results=10):
    # ایجاد سرویس جستجوی گوگل با استفاده از API Key و CSE ID
    service = build("customsearch", "v1", developerKey=api_key)
    start_index = 1  # از صفحه اول شروع می‌کنیم
    results = []

    while len(results) < num_results:
        # فراخوانی جستجو با start_index برای صفحه‌بندی
        res = service.cse().list(q=query, cx=cse_id, start=start_index, num=10).execute()
        # results.extend(res['items'])  # اضافه کردن نتایج جدید به لیست
        if 'items' in res:
            for item in res['items']:
                link = item['link']
                if 'eitaa.com' in link:  # فیلتر کردن لینک‌های مربوط به ایتا
                    results.append(link)

        # به صفحه بعد برویم
        start_index += 10

        # اگر نتایج جدید نباشد، حلقه را متوقف می‌کنیم
        if 'items' not in res:
            break



    return results
