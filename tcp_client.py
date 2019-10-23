from socket import *
sockfd=socket()
server_addr=("0.0.0.0", 8888)
sockfd.connect(server_addr)
while True:
    date=input(">>请输入消息：")
    sockfd.send(date.encode())
    if date=="##":
        break
    msg=sockfd.recv(1024)
    print("服务器：",msg.decode())
sockfd.close()
print(“你好”)
