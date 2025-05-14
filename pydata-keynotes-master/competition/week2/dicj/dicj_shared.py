"""
# 題目:幸運博彩毛收入

- 使用 Pandas 載入 XML 檔案並統計
- 使用 open 方法寫入 txt 檔
"""

import pandas as pd
import os


def parse_data(from_year, to_year):

    df = pd.DataFrame()

    path = os.path.dirname(__file__)

    for year in range(from_year, to_year + 1):
        doc = pd.read_xml(os.path.join(
            path, "outputs", f"report_cn_{year}.xml"), xpath="//STATISTICS/REPORT/DATA/RECORD", names=['month_label', 'current_monthly_income', 'prev_monthly_income', 'delta_monthly', 'current_accum_income', 'prev_accum_income', 'delta_accum'])

        # Mass convert values
        for column in ['current_monthly_income', 'prev_monthly_income', 'current_accum_income', 'prev_accum_income']:
            doc[column] = doc[column].str.replace(',', '').astype(
                int)

        doc['month'] = doc.index
        doc['month'] = doc['month'].apply(lambda x: x+1)
        doc['year'] = year

        df = pd.concat([df, doc], ignore_index=True)

    return df
