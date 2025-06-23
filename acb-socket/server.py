
import socket
import pickle
import datetime
import threading
import json

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

list_of_workers = []
list_of_cli_socket = []
list_of_cli_addr = []

with open('config.json', 'r') as f:
    config = json.load(f)
    print(f"HOST: {config['HOST']}, PORT: {config['PORT']}")

def handle_client(cli_socket, cli_addr):
    print(f"handle_client:: cli_socket: {cli_socket}, cli_addr: {cli_addr}")
    with cli_socket:
        while True:
            thread_id = threading.__name__
            #print(f"['{thread_id}'] Connected by", cli_addr)
            data = cli_socket.recv(1024)
            data_to_dict = pickle.loads(data)
            #print(f"type: {data_to_dict['type']} cmd: {data_to_dict['cmd']}")
            # To handle requests
            if data_to_dict['type'] == "request":
                #print("[From ClientA] Srv Rcvd Data: ", data_to_dict)
                data_to_dict["time"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
                #print("[To   ClientB] Srv Sent Data: ", data_to_dict)
                if not data:
                    break
                dict_to_data = pickle.dumps(data_to_dict)
                
                # Send data for processing to Worker Client
                list_of_cli_socket[1].sendall(dict_to_data)
                if data_to_dict["cmd"] == "bye":
                    print(f"Client [{cli_addr}] Terminated")
                    cli_socket.close()
                    break

            elif data_to_dict['type'] == "response":
                if data_to_dict['cmd'] == "bye":
                    cli_socket.close()
                    break

                #print(f"[From ClientB] Srv Rcvd Data: data[{data_to_dict}]")
                data_to_dict["time"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
                #print(f"[To ClientA] Srv Send Data: data[{data_to_dict}]")
                dict_to_data = pickle.dumps(data_to_dict)
                list_of_cli_socket[0].sendall(dict_to_data)
                

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((config['HOST'], config['PORT']))
    s.listen()
    for i in range(2):
        cli_socket, cli_addr = s.accept()
        print(f"main:: {cli_socket}, cli_addr: {cli_addr}")
        worker_thread = threading.Thread(target=handle_client, args=(cli_socket, cli_addr))
        worker_thread.start()
        list_of_workers.append(worker_thread)
        list_of_cli_socket.append(cli_socket)
        list_of_cli_addr.append(cli_addr)

print("----------Waiting for all thread to finish----------")
for t in list_of_workers:
    t.join()
