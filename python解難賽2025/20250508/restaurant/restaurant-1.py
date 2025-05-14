import untangle
import pandas as pd

data = untangle.parse("dst_restaurant.xml")
restaurants = data.mgto.restaurant

print(len(restaurants))

df = pd.read_xml("dst_restaurant.xml")
print(df)

