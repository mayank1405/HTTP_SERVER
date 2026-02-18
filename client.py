import socket


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address=("localhost",3000)

s.connect(address)

while True:
    msg=input("Enter msg")
    s.send(msg.encode())
    x=s.recv(1024).decode()
    print("Server Responded:",x)
    




