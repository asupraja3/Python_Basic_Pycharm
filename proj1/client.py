import socket
c = socket.socket()
c.connect(('localhost', 9999))
name = input("Enter your name: ")
c.send(name.encode())
print(c.recv(1024).decode())