# https://xml.smg.gov.mo/c_actual_brief.xml
# use untangle to parse the xml
# and get back the current temperature value

import untangle

url = "https://xml.smg.gov.mo/c_actual_brief.xml"
data = untangle.parse(url)

# get the first temperature value
Temperature = data.ActualWeatherBrief.Custom.Temperature
# check if Temperature is list or Element
if isinstance(Temperature, list): # use type(Temperature)==list also ok
    temp = Temperature[0].Value.cdata
else:
    temp = Temperature.Value.cdata


# print(dir(data))
print(f"當前溫度是{temp}°C")
