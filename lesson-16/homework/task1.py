import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print(customers_df.head(10))  # First 10 rows
conn.close()

iris_df = pd.read_json("iris.json")
print("Shape of iris dataset:", iris_df.shape)
print("Column names:", iris_df.columns)

titanic_df = pd.read_excel("titanic.xlsx")
print(titanic_df.head())

flights_df = pd.read_parquet("flights.parquet")
print(flights_df.info())

movie_df = pd.read_csv("movie.csv")
print(movie_df.sample(10))



# part2
iris_df.columns = iris_df.columns.str.lower()

iris_selected = [['sepal_length', 'sepal_width']]

print(iris_selected.head())


titanic_df30 = titanic_df[titanic_df["Age"] > 30]

from collections import Counter
value_counts = Counter(titanic_df["Sex"])
print(value_counts)


flights_selected = flights_df[['origin', 'dest', 'carrier']]

unique_destinations = flights_df['dest'].nunique()

print(flights_selected.head())
print("Number of unique destinations:", unique_destinations)


movieDur = movie_df[movie_df["duration"] > 120]
sorted_long_movies = movieDur.sort_values(by='director_facebook_likes', ascending=False)

print(sorted_long_movies.head())


# part 3
age_min = titanic_df['Age'].min()
age_max = titanic_df['Age'].max()
age_sum = titanic_df['Age'].sum()

print(f"Min age: {age_min}, Max age: {age_max}, Sum of ages: {age_sum}")


missing_values = flights_df.isnull().sum()

flights_df['air_time'].fillna(flights_df['air_time'].mean(), inplace=True)

print("Missing values before filling:\n", missing_values)
print("Missing values after filling:\n", flights_df.isnull().sum())



