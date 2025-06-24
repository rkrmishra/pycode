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
        user_input = input("[ClientA] Enter number: ")
        start_time = datetime.datetime.now()
        if user_input.isdigit():
            user_input = int(user_input)
            cmd = ""
        else:
            user_input = 0
            cmd = "bye"
        data = {
            "type": "request",
            "data": user_input,
            "cmd": cmd,
            "time": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
            }
        print('[ClientA] Send to Srv: ', data)
        dict_to_data = pickle.dumps(data)
        s.sendall(dict_to_data)
        if data['cmd'] == "bye":
            s.close()
            break
        rcv_data = s.recv(1024)
        end_time = datetime.datetime.now()
        print('[ClientA] Rcvd from Srv: ', pickle.loads(rcv_data))
        print(f"[ClientA] Time taken: {end_time - start_time}")