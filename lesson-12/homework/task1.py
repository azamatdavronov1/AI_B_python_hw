from bs4 import BeautifulSoup
import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), "weather.html")

with open(file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

table_rows = soup.find("tbody").find_all("tr")

weather_data = []

for row in table_rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temperature = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    weather_data.append({"Day": day, "Temperature": temperature, "Condition": condition})

df = pd.DataFrame(weather_data)

print("Weather Forecast:")
print(df)

max_temp = df["Temperature"].max()
hottest_days = df[df["Temperature"] == max_temp]["Day"].tolist()
print(f"\nHottest day(s): {', '.join(hottest_days)} with {max_temp}°C")

sunny_days = df[df["Condition"] == "Sunny"]["Day"].tolist()
print(f"\nSunny day(s): {', '.join(sunny_days)}")

average_temp = df["Temperature"].mean()
print(f"\nAverage Temperature for the week: {average_temp:.2f}°C")
