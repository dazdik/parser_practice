import pandas as pd

data = pd.read_html('https://parsinger.ru/table/5/index.html', header=0)
df = data[0]

sum_dict = {i: df[i].sum().astype(float).round(3) for i in df.columns}
print(sum_dict)
