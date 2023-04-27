import plotly.express as px
#from plotly import offline
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()
    
    df = px.data.iris()
    fig = px.scatter(df, x = rw.x_values, y = rw.y_values)
    
    fig.show()
    
    #offline.plot({"data" : data, "layout" : layout}, filename = "randomWalk.html")
    