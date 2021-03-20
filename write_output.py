import json

def write_output(json_data):
    with open('file.json','w') as file:
        json.dump(json_data,file)