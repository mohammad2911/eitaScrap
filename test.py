from googleapiclient.discovery import build

# تنظیمات API Key و CSE ID
api_key = 'AIzaSyBM4_VSs1zQUNiFr26YaLKJrn_ae-xdISo'  # API Key خود را وارد کنید
cse_id = '36f9b1acc1d9c41b0'  # CSE ID خود را وارد کنید

# ساخت سرویس جستجوی گوگل
def google_search(query, api_key, cse_id, num_results=10):
    service = build("customsearch", "v1", developerKey=api_key)
    start_index = 1  # از صفحه اول شروع می‌کنیم
    results = []

    while len(results) < num_results:
        # فراخوانی جستجو با start_index برای صفحه‌بندی
        res = service.cse().list(q=query, cx=cse_id, start=start_index, num=10).execute()
        results.extend(res['items'])  # اضافه کردن نتایج جدید به لیست

        # به صفحه بعد برویم
        start_index += 10

        # اگر نتایج جدید نباشد، حلقه را متوقف می‌کنیم
        if 'items' not in res:
            break

    return results


# جستجوی کلمه "قرض الحسنه site:eitaa.com" در گوگل برای محدود کردن به ایتا
query = "قرض الحسنه site:eitaa.com"  # اینجا می‌توانید هر کلمه‌ای که می‌خواهید جستجو کنید را وارد کنید
results = google_search(query, api_key, cse_id, num_results=30)  # مثلا 30 نتیجه می‌خواهیم

# استخراج و چاپ لینک‌های کانال‌ها و گروه‌های ایتا
for result in results:
    link = result['link']
    # بررسی اینکه آیا لینک به ایتا مربوط است
    if "eitaa.com" in link:
        print(f"Found eitaa link: {link}")