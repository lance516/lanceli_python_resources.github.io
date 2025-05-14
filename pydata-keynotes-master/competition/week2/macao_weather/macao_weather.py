"""
# 題目：七日天氣

- 使用 Requests 下載資料
- 使用 Untangle 讀取 XML 檔案
- 使用 Beautiful Soup 讀取 HTML 檔案
"""

import os
import requests
from bs4 import BeautifulSoup
import untangle


def parse_weather_status():
    mappings = {}

    url = 'http://localhost:8000/weather/weather_status.html'
    page = requests.get(url)
    page.encoding = "utf-8"  # force encoding
    soup = BeautifulSoup(page.text, 'html.parser')

    # find an element a[name=WeatherStatus]
    title = soup.find("a", {"name": "WeatherStatus"})

    if title != None:
        # find next element with tag <table> regardless of level
        table_rows = title.find_next("table").select('tr')
        if table_rows != None:
            for row in table_rows:
                # find all td in current row
                cols = row.find_all("td")

                if(cols[0].text != "Code"):  # Skip the row with text "Code"
                    key = cols[0].text
                    value = cols[1].text
                    mappings[key] = value

    return mappings


def parse_weather(mappings={}):
    url = 'http://localhost:8000/weather/c_7daysforecast.xml'
    page = requests.get(url)
    page.encoding = "utf-8"  # force encoding

    seven_days_forecast = []
    doc = untangle.parse(page.text)
    for row in doc.SevenDaysForecast.Custom.WeatherForecast:

        date = row.ValidFor.cdata
        raw_status = row.WeatherStatus.cdata
        status_label = mappings[raw_status]

        high_temperature = None
        low_temperature = None

        # Loop through temperature tags for determine high and low temperature
        for temp in row.Temperature:
            if temp.Type.cdata == "1":  # high
                high_temperature = temp.Value.cdata
            elif temp.Type.cdata == "2":  # low
                low_temperature = temp.Value.cdata

        seven_days_forecast.append({
            'date': date,
            'status': status_label,
            'low_temperature': low_temperature,
            'high_temperature': high_temperature
        })

    return seven_days_forecast


def write_data(data):
    # get the file location of the python script
    path = os.path.dirname(__file__)

    for row in data:
        filename = f"forecast-{row['date']}.txt"
        with open(os.path.join(path, "outputs", filename), 'w') as f:
            f.write(
                f"{row['date']} ({row['status']}) {row['low_temperature']} 至 {row['high_temperature']} 度")


def main():
    weather_status = parse_weather_status()
    forecast = parse_weather(weather_status)
    write_data(forecast)


if __name__ == "__main__":
    main()
