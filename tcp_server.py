import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#端口立即重用,需要在bind之前使用（仅适用tcp套接字）
sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sockfd.bind(("127.0.0.1", 8873))
sockfd.listen(5)
while True:
    print("Waiting for connect...")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        break
    while True:
        date = connfd.recv(5)
        if not date:
            break
        print("Receive:", date.decode())
        n = connfd.send(b"Thanks")
        print("Send %d bytes" % n)
    connfd.close()
sockfd.close()
