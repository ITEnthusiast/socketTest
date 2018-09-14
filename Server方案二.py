import socket

socketServer = socket.socket()
address = ('127.0.0.1', 8002)
socketServer.bind(address)  # 将服务端 socket 绑定到制定 ip 地址
socketServer.listen(3)  # 开始监听传入的连接，参数决定在关闭前可以连接客户端的最大数量，这个数值不能无限大
print('Wating For Client...')

while 1:
    socketClient, addressClient = socketServer.accept()  # 阻塞等待客户端来访问
    print('=' * 6, '\t各部门注意：', socketClient.getpeername(), '来了\t', '=' * 6)
    socketClient.send(bytes('方案二为您服务：来约啊', 'utf8'))
    while 1:
        # try:
        recvData = socketClient.recv(1024)
        # except Exception :
        #     break
        print(socketClient.getpeername(), str(recvData, 'utf8'))
        if not recvData:
            break
        inputStr = input(socketClient.getsockname())
        socketClient.send(bytes(inputStr, 'utf8'))

socketClient.close()  # 关闭与当前客户端的连接通道

