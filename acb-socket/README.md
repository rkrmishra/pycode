# acb-socket

A Python project for working with sockets, implemented for basic analysis of packets using Wireshark. This is only for learning purpose.

## Features

- Simple socket server and client implementation
- Suitable for learning and prototyping network applications
- Depicts:
    - Physical Structure: `Client <-> Server <-> Client`
    - Logical Structure: `Client <-> Broker <-> Server`

## Requirements

- Python 3.7+
- No external dependencies (unless you add them)

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/acb-socket.git
cd acb-socket
```

(Optional) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Bring up ststem in following order

### Server

```bash
python server.py
```

### ClientA

```bash
python clientA.py
```
Do give any input untill you start the `clientB.py`

### ClientB

```bash
python clientB.py
```

## Project Structure

```
acb-socket/
├── clientA.py
├── clientB.py
├── server.py
├── config.json
├── README.md
└── ...
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

##