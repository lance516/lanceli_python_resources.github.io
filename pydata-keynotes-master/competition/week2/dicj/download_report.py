"""
# 題目:幸運博彩毛收入

- 使用 requests 下載所有 xml 檔案
"""

import requests
import os
import time


def main():
    path = os.path.dirname(__file__)
    for i in range(2010, 2022):
        url = f"http://localhost:8000/dicj/{i}/report_cn.xml"
        print(f"Downloading {url}...")
        doc = requests.get(url)
        doc.encoding = "utf-8"

        year = str(i)
        filename = f"report_cn_{year}.xml"

        with open(os.path.join(path, "outputs", filename), 'w') as f:
            f.write(doc.text)


if __name__ == "__main__":
    main()
