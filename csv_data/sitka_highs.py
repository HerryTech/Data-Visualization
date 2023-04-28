import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "csv_data/sitka_weather_2018.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
#Get high temperature
    highs = []
    date = []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        date.append(current_date)
        highs.append(high)
    
plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(date, highs, c = "red")

plt.title("Daily high temperature, 2018", fontsize = 24)
plt.xlabel("Date", fontsize = 14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)

plt.savefig("csv_data/sitka_highs.png")