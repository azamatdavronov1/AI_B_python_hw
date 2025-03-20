# import pandas as pd
#
# # Titanic Pipeline
# titanic = pd.read_csv("titanic.csv")
# result_titanic = (
#     titanic[titanic["Survived"] == 1]
#     .assign(Age=lambda x: x["Age"].fillna(x["Age"].mean()))
#     .assign(Fare_Per_Age=lambda x: x["Fare"] / x["Age"])
# )
#
# # Flights Pipeline
# flights = pd.read_csv("flights.csv")
# result_flights = (
#     flights[flights["DepDelay"] > 30]
#     .assign(Delay_Per_Hour=lambda x: x["DepDelay"] / x["ActualElapsedTime"])
# )

