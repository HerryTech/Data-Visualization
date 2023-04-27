import csv
import matplotlib.pyplot as plt

filename = "Data/sitka_weather.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
#Get high temperature
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
    
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot("highs", c = "red")