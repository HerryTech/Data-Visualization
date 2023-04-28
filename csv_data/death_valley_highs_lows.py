import csv
from datetime import datetime 
import matplotlib.pyplot as plt

filename = "csv_data/death_valley_2018.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
#for index, column_header in enumerate(header_row):
    #print(index, column_header)
    
    date, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            date.append(current_date)
            highs.append(high)
            lows.append(low)
        
plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(date, highs, c = "red", alpha = 0.5)
ax.plot(date, lows, c ="blue", alpha = 0.5)

plt.fill_between(date, highs, lows, facecolor = "blue", alpha = 0.5)
plt.title("Daily high and low temperature, 2018", fontsize = 24)
plt.xlabel("Date", fontsize = 14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)

plt.savefig("csv_data/deathValley_highs_lows.png")
