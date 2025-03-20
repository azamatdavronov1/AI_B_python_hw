# import pandas as pd
#
# # Titanic Age Group
# titanic = pd.read_csv("titanic.csv")
# titanic["Age_Group"] = titanic["Age"].apply(lambda x: "Child" if x < 18 else "Adult")
#
# # Employee Salary Normalization
# employees = pd.read_csv("employee.csv")
# employees["NormalizedSalary"] = employees.groupby("Department")["Salary"].transform(
#     lambda x: (x - x.min()) / (x.max() - x.min())
# )
#
# # Movie Duration Classification
# movies = pd.read_csv("movie.csv")
# movies["Duration_Class"] = movies["duration"].apply(
#     lambda x: "Short" if x < 60 else "Medium" if 60 <= x <= 120 else "Long"
# )

