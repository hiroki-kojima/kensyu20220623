import json
def read():
    with open('mydata.json', mode='rt', encoding='utf-8') as file:
        data = json.load(file)
        return data
def write(time, name, message):
    weight_dict ={"time":time,"name":name,"message":message}
    with open('mydata.json', 'r') as f:
        read_data = json.load(f)

    save_data = [read_data, weight_dict]

    with open('mydata.json', 'w') as f:
        json.dump(save_data, f)