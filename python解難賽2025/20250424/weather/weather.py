

import untangle
import requests

from bs4 import BeautifulSoup
url = "https://xml.smg.gov.mo/c_7daysforecast.xml"
data = untangle.parse(url)

url_status = "https://xml.smg.gov.mo"
response = requests.get(url_status)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, from_encoding="utf-8")
status = soup.find_all("table")[-1]



weatherforecast = data.SevenDaysForecast.Custom.WeatherForecast
for day in weatherforecast:
    date = day.ValidFor.cdata
    high_temperature = None
    low_temperature = None
    for temp in day.Temperature:
        if temp.Type.cdata == "1":
            high_temperature = temp.Value.cdata
        elif temp.Type.cdata == "2":
            low_temperature = temp.Value.cdata
    weatherdiscription = day.WeatherDescription.cdata
    weatherstatus = day.WeatherStatus.cdata
    # from the status table, using the value of weatherstatus (which is the Code of WeatherStatus, is a string) to get the description
    for tr in status.find_all("tr"):
        if tr.td.text == weatherstatus:
            weatherstatus = tr.find_all("td")[1].text
            break
    
    print(f"{date} {low_temperature}°C ~ {high_temperature}°C {weatherstatus} {weatherdiscription}")

