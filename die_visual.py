from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
x_values = list(range(1, die.num_sides+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {"title" : "Result"}
y_axis_config = {"title" : "Frequency of Result"}
my_layout = Layout(title = "Result of rolling a die 1000 times", xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({"data" : data, "layout" : my_layout}, filename = "die.html")
    