import pandas as pd
from sqlalchemy import create_engine

# Считываем данные из Excel файла
df = pd.read_excel('путь_к_файлу.xlsx')

# Устанавливаем соединение с базой данных MySQL
engine = create_engine('mysql://username:password@localhost/db_name')

# Записываем данные в базу данных MySQL
df.to_sql('название_таблицы', con=engine, if_exists='replace', index=False)