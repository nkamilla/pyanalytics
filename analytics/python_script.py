import pandas as pd
from sqlalchemy import create_engine

# Подключаемся к базе данных
engine = create_engine('postgresql://user:password@db:5432/movielens')

# Загружаем данные
ratings = pd.read_csv('./ratings.csv')  # Путь к ratings.csv
movies = pd.read_csv('./movies.csv')    # Путь к movies.csv

# Импортируем данные в базу
ratings.to_sql('ratings', engine, if_exists='replace', index=False)
movies.to_sql('movies', engine, if_exists='replace', index=False)

print("Данные успешно импортированы!")

