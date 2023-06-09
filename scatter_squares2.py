import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = (0, 0.8, 0), s = 100)

ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of values", fontsize = 14)

plt.show()