import socket
import select



address=("localhost", 3000)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(address)
s.listen(1)
print(s.getsockname())





while True:
    ready_sockets, _, _=select.select(
        [s],
        [],
        [],
        0
    )

    if ready_sockets:
        for mysocket in ready_sockets:

            socket_obj,sock_address= mysocket.accept()

            client_msg=socket_obj.recv(1024).decode()
            print("Client address:", sock_address)
            print("Client said:", client_msg)

            msg=f""" HTTP/1.1 200 OK\r\nContent-type: text/html\r\nSet-Cookie: ServerName=MayankTestServer\r
                      \r\n
                      <!doctype html>
                      <head>
                      <title>Mayank's Test Server</title>
                      </head>

                      <body>
                        <h1>Welcome to Mayank's test http server</h1>
                        <h2>Server Address: {address}</h2>
                        <h2> Connected thru(Client Address): {sock_address} </h2>
                        <pre> {client_msg}</pre>
                        <h1>this is part of client msg</h1>
                      </body> 



            """
            socket_obj.sendall(msg.encode())

            try:
                socket_obj.close()
            except OSError:
                pass
            

        


