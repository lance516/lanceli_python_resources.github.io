"""
# 題目:幸運博彩毛收入

- 使用 Pandas 載入 XML 檔案，並轉統計
- 使用 open 方法寫入 txt 檔
"""

import pandas as pd
import os
from dicj_shared import parse_data


def write_data(df):

    path = os.path.dirname(__file__)
    df.to_excel(os.path.join(path, "outputs",
                             "dicj_average.xlsx"), header=False)


def main():

    df = parse_data(2010, 2021)

    # First group by year, and find the average(mean) for current_monthly_income column only
    average_df = df.groupby(['year'])['current_monthly_income'].mean()

    write_data(average_df)


if __name__ == "__main__":
    main()
