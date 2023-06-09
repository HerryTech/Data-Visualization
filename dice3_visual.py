import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
x_values = list(range(2, max_result+1))

plt.style.use("classic")
fig, ax = plt.subplots()
ax.barh(x_values, frequencies, color = "brown")

ax.set_title("Result of rolling two dice 1000 times", fontsize = 24)
ax.set_xlabel("Result", fontsize = 14)
ax.set_ylabel("Frequency of Result", fontsize = 14)

plt.savefig("dice3.png")