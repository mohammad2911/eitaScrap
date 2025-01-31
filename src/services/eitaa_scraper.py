import re

def extract_channel_ids1(links):
    channel_ids = []
    for link in links:
        if 'eitaa.com' in link:
            # فرض می‌کنیم ایدی در انتهای URL قرار دارد
            channel_id = link.split('/')[-1]
            channel_ids.append(channel_id)
    return channel_ids

def extract_eitaa_ids(links):
    ids = []
    for link in links:
        print(link)
        # استفاده از regex برای استخراج آیدی
        match = re.search(r'eitaa\.com/(joinchat/)?([a-zA-Z0-9_-]+)', link)
        if match:
            print(match.group(2))
            ids.append(match.group(2))  # گروه دوم شامل آیدی است
    return ids
