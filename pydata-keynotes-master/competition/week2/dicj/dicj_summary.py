"""
# 題目:幸運博彩毛收入

- 使用 Pandas 載入 XML 檔案並統計
- 使用 open 方法寫入 txt 檔
"""

import pandas as pd
import os
from dicj_shared import parse_data


def write_data(min_row, max_row):

    min_row_text = f"最低值：{min_row['current_monthly_income']}，於{min_row['year']}年{min_row['month']}月發生。\n"
    max_row_text = f"最低值：{max_row['current_monthly_income']}，於{max_row['year']}年{max_row['month']}月發生。"

    path = os.path.dirname(__file__)
    with open(os.path.join(path, "outputs", "dicj_summary.txt"), 'w') as f:
        f.write(min_row_text)
        f.write(max_row_text)


def main():

    df = parse_data(2019, 2021)

    # Find max row
    max_row_idx = df['current_monthly_income'].idxmax()
    # Use df.loc to find row at index
    max_row = df.loc[max_row_idx]

    # Find min row
    min_row_idx = df['current_monthly_income'].idxmin()
    # Use df.loc to find row at index
    min_row = df.loc[min_row_idx]

    write_data(min_row, max_row)


if __name__ == "__main__":
    main()
