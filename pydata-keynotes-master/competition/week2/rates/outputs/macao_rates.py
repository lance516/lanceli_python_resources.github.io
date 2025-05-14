"""
# 題目:匯率

- 使用 request 讀取滙率網頁
- 使用 Beautiful Soup 取得滙率資料
"""

import requests
from bs4 import BeautifulSoup


def parse_rates():
    page = requests.get('http://localhost:8000/rates/rates.html')
    page.encoding = "utf-8"
    doc = BeautifulSoup(page.text, 'html.parser')
    table = doc.find("table")

    rates = {}
    if table != None:
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) > 0:  # Determine if it is header or not
                label = columns[1].text  # 貨幣

                sell_rate = None
                try:
                    sell_rate = float(columns[7].text) / 100  # 賣出價
                except:
                    pass  # Do nothing

                # rates.append({
                #     'currency': label,
                #     'sell_rate': sell_rate,
                # })
                rates[label] = sell_rate

    return rates


def latest_cny_mop():
    rates = parse_rates()
    return rates['澳門元/人民幣']


def main():
    rates = parse_rates()
    print(rates)


if __name__ == "__main__":
    main()
