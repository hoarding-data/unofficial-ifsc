import json

YEAR_FOLDER="ifsc_year_data"

full_data = dict()
with open('full_data.json') as fh:
    full_data = json.load(fh)

for year in full_data.keys():
    year_object = full_data[year]
    filename = "{}/ifsc_{}_data.json".format(YEAR_FOLDER,year)
    with open(filename, "w") as fh:
        fh.write(json.dumps(year_object))
    
