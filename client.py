import json
import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

config = json.load(open("config.json"))
server_address = config["server_socket_path"]
address = config["client_socket_path"]

try:
    os.unlink(address)
except FileNotFoundError:
    pass

input_text = input("何か入力してください：")
message = input_text.encode("utf-8")

sock.bind(address)

try:
    sent = sock.sendto(message, server_address)
    print("応答待ち")
    data, server = sock.recvfrom(4096)
    print(data.decode("utf-8"))

finally:
    print("ソケットを閉じる")
    sock.close