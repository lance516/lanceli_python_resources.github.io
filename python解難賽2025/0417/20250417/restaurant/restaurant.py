# this file reads the dst_restaurant.xml file
# using DataFrame

import pandas as pd
import numpy as np

# read the xml file
xml_file = 'dst_restaurant.xml'

# the main program
if __name__ == '__main__':
    df = pd.read_xml(xml_file)
    target_columns = ["id", "name_cn", "dish_name_zh"]
    # randomly pick one row
    row = df[target_columns].sample(1)
    name = row['name_cn'].values[0]
    dish = row['dish_name_zh'].values[0]
    if dish == None:
        print(f"今晚一於去{name}吃啦！")
    else:
        print(f"今晚一於去{name}吃{dish}菜啦！")