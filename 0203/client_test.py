import socket

ADDRESS = ('localhost', 8080)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

body = f'''GET / HTTP/1.1
Host: {':'.join(map(str,ADDRESS))}'''
client.sendall(body.encode('utf-8'))

while True:
    response = client.recv(1024)
    if not response:
        break
    print(response.decode('utf-8'), end='')

client.close()