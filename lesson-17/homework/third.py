
# import pandas as pd
#
# # Titanic Grouping
# titanic = pd.read_csv("titanic.csv")
# grouped_titanic = titanic.groupby("Pclass").agg(
#     AverageAge=("Age", "mean"),
#     TotalFare=("Fare", "sum"),
#     PassengerCount=("PassengerId", "count")
# ).reset_index()
#
# # Movie Multi-level Grouping
# movies = pd.read_csv("movie.csv")
# grouped_movies = movies.groupby(["color", "director_name"]).agg(
#     TotalReviews=("num_critic_for_reviews", "sum"),
#     AverageDuration=("duration", "mean")
# ).reset_index()
#
# # Flights Nested Grouping
# flights = pd.read_csv("flights.csv")
# grouped_flights = flights.groupby(["Year", "Month"]).agg(
#     TotalFlights=("Flight", "count"),
#     AverageArrivalDelay=("ArrDelay", "mean"),
#     MaxDepartureDelay=("DepDelay", "max")
# ).reset_index()
