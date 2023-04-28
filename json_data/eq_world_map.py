import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "json_data/eq_30.json"
with open(filename) as f:
    eq_1_data = json.load(f)

eq_dicts = eq_1_data["features"]

mags, lons, lats, hover_texts = [], [], [], []
for all in eq_dicts:
    mag = all["properties"]["mag"]
    lon = all["geometry"]["coordinates"][0]
    lat = all["geometry"]["coordinates"][1]
    title = all["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

data = [{
    "type" : "scattergeo",
    "lon" : lons,
    "lat" : lats,
    "text" : hover_texts,
    "marker" : {
        "size" : [5 * mag for mag in mags],
        "color" : mags,
        "colorscale" : "Viridis",
        "reversescale" : True,
        "colorbar" : {"title" : "Magnitude"}
    },
}]
my_layout = Layout(title = "Global Earthquake")
fig = {"data" : data, "layout" : my_layout}
offline.plot(fig, filename = "global_earthquake.html")