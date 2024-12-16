from faker import Faker
import json
import os
import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

config = json.load(open("config.json"))
server_address = config["server_socket_path"]
fake = Faker("ja-jp")

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"開始： {server_address}")

sock.bind(server_address)

try:
    while True:
        print("受信待ち")
        data, address = sock.recvfrom(4096)
        print(f"バイト数： {len(data)} アドレス： {address}")
        print(data.decode("utf-8"))

        if data:
            new_data = fake.name().encode("utf-8")
            sent = sock.sendto(new_data, address)
            print(f"バイト数： {sent} アドレス： {address}")
except KeyboardInterrupt:
    sys.exit()
