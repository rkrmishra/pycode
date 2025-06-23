import socket
import datetime
import pickle
import json

with open('config.json', 'r') as f:
    config = json.load(f)
    print(f"HOST: {config['HOST']}, PORT: {config['PORT']}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((config['HOST'], config['PORT']))
    while True:
        print("[ClientB] Waiting for Request data...")
        data = s.recv(1024)
        data_to_dict = pickle.loads(data)

        print('[ ClientB] Rcvd Data From Srv: ', data_to_dict)
        data_to_dict['type'] = "response"
        data_to_dict['data'] = data_to_dict['data'] * data_to_dict['data']
        data_to_dict['time'] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
        cmd = ""
        print('[ ClientB] Send Data to Srv: ', data_to_dict)

        dict_to_data = pickle.dumps(data_to_dict)
        s.sendall(dict_to_data)

        if data_to_dict['cmd'] == "bye":
            s.close()
            break