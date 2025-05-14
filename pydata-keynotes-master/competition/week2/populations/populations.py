"""
# 題目:人口數據

- 使用 Pandas 讀取 csv 檔案，分析並輸出 Excel 檔案
"""

import pandas as pd
import os

# 讀取 CSV 做基本處理


def read_countries(path, filename):
    file_path = os.path.join(path, filename)

    df = pd.read_csv(file_path)

    # rename first column name
    new_columns = list(df.columns)  # convert Index to list
    new_columns[0] = "country"
    df.columns = new_columns

    value_only_columns = new_columns[1:]
    df[value_only_columns] = df[value_only_columns].transform(
        lambda x: x * 1000)

    df = df.set_index('country')

    return df


# 全球總人口數 Excel

def write_global_population(path, df):
    filename = "global-population.xlsx"
    file_path = os.path.join(path, filename)

    new_df = df.sum()  # sum all columns
    new_df.to_excel(file_path, header=False)  # write to excel

# 趨勢折線圖


def plot_global_population(path, df):

    new_df = df.transform(
        lambda x: x / 1000000).sum()

    ax = new_df.plot(xlabel="Year", ylabel="Population (in millions)",
                     marker="o")
    fig = ax.get_figure()
    fig.savefig(os.path.join(path, "global-population.png"))

# 全球頭十位 Excel


def write_topten_population(path, df):

    with pd.ExcelWriter(os.path.join(path, "top-10-population.xlsx")) as writer:

        pd.DataFrame([('這個檔案列出各年全球人口頭十位的國家。')]).to_excel(
            writer, sheet_name='Summary', header=False, index=False)

        for year in df.columns:
            # This method is equivalent to df.sort_values(columns, ascending=False).head(n), but more performant.
            new_df = df.nlargest(10, year)[year]
            new_df.to_excel(
                writer, sheet_name=f"{year}年", index_label='國家', header=['人口'])


def main():
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, "inputs")
    out_file_path = os.path.join(path, "outputs")

    df = read_countries(file_path, "countries.csv")

    write_global_population(out_file_path, df)
    plot_global_population(out_file_path, df)
    write_topten_population(out_file_path, df)


if __name__ == "__main__":
    main()
