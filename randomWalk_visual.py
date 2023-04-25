import matplotlib.pyplot as plt
from random_walk import RandomWalk

#keep making new walks as long as the program is active
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize = (15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = "none", s = 1)
    #Emphasis the first and last point
    ax.scatter(0, 0, c = "green", edgecolors = "none", s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c= "red", edgecolors = "none", s = 100)
    
    #Remove axes
    ax.xaxis.set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    #Set title
    ax.set_title("A Random Walk", fontsize = 24)

    plt.savefig("random_walk.png")
    
    keep_walking = input("Do you want to take another walk? y/n: ")
    if keep_walking == "n":
        break