import json
with open("data.json", mode="r") as data_file:
    # writing to the data file
    # json.dump(new_data, data_file, indent=4)
    # updating a data file
    data = json.load(data_file)
    # data.update(new_data)

with open("data.json", mode="w") as data_file:
    json.dump(data, data_file, indent=4)