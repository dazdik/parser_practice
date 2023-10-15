import pandas as pd

data = pd.read_html('https://parsinger.ru/4.8/6/index.html', header=0, encoding='utf-8')

# выборка интересующих столбцов и сортировка по стоимости от меньшего к большему
selected_columns = ['Марка Авто', 'Год выпуска', 'Тип двигателя', 'Стоимость авто']
df = data[0].sort_values(by='Стоимость авто')[selected_columns]

# фильтрация авто по стоимости, году выпуска и типу двигателя,
filtered_df = df.loc[(df['Стоимость авто'] <= 4000000)
                     & (df['Год выпуска'] >= 2005)
                     & (df['Тип двигателя'] == 'Бензиновый')]

# вывод данных в формате json
json_data = filtered_df.to_json(orient='records', force_ascii=False, indent=4)
print(json_data)
