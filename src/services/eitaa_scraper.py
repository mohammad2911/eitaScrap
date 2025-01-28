def extract_channel_ids(links):
    channel_ids = []
    for link in links:
        if 'eitaa.com' in link:
            # فرض می‌کنیم ایدی در انتهای URL قرار دارد
            channel_id = link.split('/')[-1]
            channel_ids.append(channel_id)
    return channel_ids
