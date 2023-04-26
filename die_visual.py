from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
x_values = list(range(1, die.num_sides+1))
data = [Bar(x = x_values, y = frequencies)]
    