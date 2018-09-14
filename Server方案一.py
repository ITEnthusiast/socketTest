import socket

socketServer = socket.socket()
address = ('127.0.0.1', 8001)
socketServer.bind(address)  # 将服务端 socket 绑定到制定 ip 地址
socketServer.listen(3)  # 开始监听传入的连接，参数决定在关闭前可以连接客户端的最大数量，这个数值不能无限大
print('Wating For Client...')

socketClient, addressClient = socketServer.accept()  # 阻塞等待客户端来访问
''' accept() -> (socket object, address info) '''
print('='*6, '\t各部门注意：', socketClient.getpeername(), '来了\t', '='*6)
socketClient.send(bytes('方案一为您服务：来约啊', 'utf8'))
# print('socketServer: ', socketServer)
# print('socketClient: ', socketClient)
# print('addressClient: ', addressClient)
'''
    socketServer:   <socket.socket fd=3, 
                    family=AddressFamily.AF_INET, 
                    type=SocketKind.SOCK_STREAM, 
                    proto=0, 
                    laddr=('127.0.0.1', 8000)>

    socketClient:   <socket.socket fd=4, 
                    family=AddressFamily.AF_INET, 
                    type=SocketKind.SOCK_STREAM, 
                    proto=0, 
                    laddr=('127.0.0.1', 8000), 
                    raddr=('127.0.0.1', 50737)>

    addressClient:  ('127.0.0.1', 50737)
'''

# python3中，不管是 server 端，还是 client 端的send()、recv()方法传送的内容均为字节
while 1:
    recvData = socketClient.recv(1024)
    if not recvData:
        socketClient, addressClient = socketServer.accept()  # 阻塞等待客户端来访问
        print('='*6, '\t各部门注意：', socketClient.getpeername(), '来了\t', '='*6)
        socketClient.send(bytes('方案一为您服务：来约啊', 'utf8'))
        continue
    print(socketClient.getpeername(), str(recvData, 'utf8'))
    inputStr = input(socketClient.getsockname())
    socketClient.send(bytes(inputStr, 'utf8'))

socketClient.close()  # 关闭与当前客户端的连接通道
# socketServer.close()  # 一般不关闭

'''
def __init__(self, family=-1, type=-1, proto=-1, fileno=None):

family = AF_INET :服务器之间的通信ip采用是IPv4
family = AF_INET6 :服务器之间的通信ip采用是IPv6
family = AF_UNIX :Unix不同进程间通信

type = SOCK_STREAM :TCP
type = SOCK_DGRAM :UDP

'''