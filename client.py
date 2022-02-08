import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.1.1', 8080))

while True:
    client.send(input().encode('utf-8'))
