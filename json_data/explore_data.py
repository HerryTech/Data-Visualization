import json

filename = "json_data/eq_1.json"
with open(filename) as f:
    eq_1_data = json.load(f)
    
"""filename = "json_data/readable_eq_1.json"
with open(filename, "w") as f:
    json.dump(eq_1_data, f, indent = 4)"""
    
eq_dicts = eq_1_data["features"]

mags, lons, lats = [], [], []
for all in eq_dicts:
    mag = all["properties"]["mag"]
    lon = all["geometry"]["coordinates"][0]
    lat = all["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
print(lats)