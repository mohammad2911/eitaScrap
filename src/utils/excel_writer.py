import pandas as pd

def save_to_excel(channel_ids, filename="channel_ids.xlsx"):
    df = pd.DataFrame(channel_ids, columns=["Channel ID"])
    df.to_excel(filename, index=False)
