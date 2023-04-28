import json

filename = "json_data/eq_1.json"
with open(filename) as f:
    eq_1_data = json.load(f)
    
"""filename = "json_data/readable_eq_1.json"
with open(filename, "w") as f:
    json.dump(eq_1_data, f, indent = 4)"""
    
eq_dicts = eq_1_data["features"]

mags =[]
for all in eq_dicts:
    mag = all["properties"]["mag"]
    mags.append(mag)
    
print(mags[:10])