import matplotlib.pyplot as plt
from random_walk import RandomWalk

#keep making new walks as long as the program is active
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = "none", s = 15)
    #Emphasis the first and last point
    ax.scatter(0, 0, c = "green", edgecolors = "none", s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c= "red", edgecolors = "none", s = 100)
    
    
    ax.set_title("Random Walk", fontsize = 24)
    ax.set_xlabel("X-steps", fontsize = 14)
    ax.set_ylabel("Y-steps", fontsize = 14)

    plt.savefig("random_walk.png")
    
    keep_walking = input("Do you want to take another walk? y/n: ")
    if keep_walking == "n":
        break