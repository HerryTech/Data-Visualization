import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "json_data/eq_30.json"
with open(filename) as f:
    eq_1_data = json.load(f)

eq_dicts = eq_1_data["features"]

mags, lons, lats = [], [], []
for all in eq_dicts:
    mag = all["properties"]["mag"]
    lon = all["geometry"]["coordinates"][0]
    lat = all["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

data = [{
    "type" : "scattergeo",
    "lon" : lons,
    "lat" : lats,
    "marker" : {
        "size" : [5 * mag for mag in mags]
    },
}]
my_layout = Layout(title = "Global Earthquake")
fig = {"data" : data, "layout" : my_layout}
offline.plot(fig, filename = "global_earthquake.html")