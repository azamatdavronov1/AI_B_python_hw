# import pandas as pd
# import sqlite3
#
# # Chinook Inner Join
# conn = sqlite3.connect("chinook.db")
# query = """
# SELECT customers.CustomerId, customers.FirstName, customers.LastName, COUNT(invoices.InvoiceId) AS TotalInvoices
# FROM customers
# INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
# GROUP BY customers.CustomerId
# """
# result = pd.read_sql_query(query, conn)
# conn.close()
#
# # Movie Outer Join
# movies = pd.read_csv("movie.csv")
# df1 = movies[["director_name", "color"]]
# df2 = movies[["director_name", "num_critic_for_reviews"]]
# left_join = pd.merge(df1, df2, on="director_name", how="left")
# full_outer_join = pd.merge(df1, df2, on="director_name", how="outer")
# print("Left Join Rows:", len(left_join), "Full Outer Join Rows:", len(full_outer_join))

