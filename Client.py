import socket

socketClient = socket.socket()
address = ('127.0.0.1', 8002)
socketClient.connect(address)
# print('socketClient: ', socketClient)
'''
    socketClient:  <socket.socket fd=3, 
                    family=AddressFamily.AF_INET, 
                    type=SocketKind.SOCK_STREAM, 
                    proto=0, 
                    laddr=('127.0.0.1', 50737), 
                    raddr=('127.0.0.1', 8000)>
'''

# python3中，不管是 server 端，还是 client 端的send()、recv()方法传送的内容均为字节
recvData = socketClient.recv(1024)
print(socketClient.getpeername(), str(recvData, 'utf8'))
while 1:
    inputStr = input(socketClient.getsockname())
    if inputStr == 'exit':
        break
    socketClient.send(bytes(inputStr, 'utf8'))

    recvData = socketClient.recv(1024)
    print(address, str(recvData, 'utf8'))

socketClient.close()    # 关闭与当前服务端的连接通道


