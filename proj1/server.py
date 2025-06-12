import socket
s=socket.socket()
print("Socket created")

s.bind(('localhost', 9999))
s.listen(3)
print("Socket is listening")

while True:
    c,addr = s.accept()
    print("Got connection from", addr)
    name = c.recv(1024).decode()
    print("Name received:", name)
    c.send(b'Thank you for connecting')
    c.close()