import requests
import os
import time


def main():
    path = os.path.dirname(__file__)
    for i in range(2010, 2022):
        url = f"https://www.dicj.gov.mo/web/cn/information/DadosEstat_mensal/{i}/report_cn.xml"
        print(f"Downloading {url}")
        doc = requests.get(url)
        doc.encoding = "utf-8"

        filename = f"report_cn.xml"

        dir = os.path.join(path, str(i))
        if not os.path.isdir(dir):
            os.makedirs(dir)
        with open(os.path.join(dir, filename), 'w') as f:
            f.write(doc.text)

        time.sleep(1)


if __name__ == "__main__":
    main()
