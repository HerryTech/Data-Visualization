import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use("classic")
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s = 10)
ax.set_title("Random Walk", fontsize = 24)
ax.set_xlabel("X-steps", fontsize = 14)
ax.set_ylabel("Y-steps", fontsize = 14)

plt.savefig("random_walk.png")