import socket
import pickle
import datetime

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        cli_socket, cli_addr = s.accept()
        with cli_socket:
            print('Connected by', cli_addr)
            data = cli_socket.recv(1024)
            data_to_dict = pickle.loads(data)
            print("Srv Rcvd Data: ", data_to_dict)
            data_to_dict["time"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
            data_to_dict["data"] =+ 100
            print("Srv Sent Data: ", data_to_dict)
            if not data:
                break
            dict_to_data = pickle.dumps(data_to_dict)
            cli_socket.sendall(dict_to_data)
