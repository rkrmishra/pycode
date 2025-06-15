import socket
import datetime
import pickle

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = {
        "type": "request",
        "data": 0,
        "time": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        }
    dict_to_data = pickle.dumps(data)
    s.sendall(dict_to_data)
    rcv_data = s.recv(1024)

print('Received', pickle.loads(rcv_data))