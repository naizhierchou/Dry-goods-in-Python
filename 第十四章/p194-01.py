import socket
# 创建socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 本地信息
address = ('', 7788)
# 绑定
tcp_server_socket.bind(address)
# 设置监听
# 使⽤socket创建的套接字默认的属性是主动的，使⽤listen将其变为被动的，这样就可以接收别⼈的
# 链接了
# 128:表示最⼤等待连接数
tcp_server_socket.listen(128)
# 如果有新的客户端来链接服务器，那么就产⽣⼀个新的套接字专⻔为这个客户端服务
# client_socket⽤来为这个客户端服务
# tcp_server_socket就可以省下来专⻔等待其他新客户端的链接
client_socket, clientAddr = tcp_server_socket.accept()
# 接收对⽅发送过来的数据
recv_data = client_socket.recv(1024) # 接收1024个字节
print('接收到的数据为:', recv_data.decode('gbk'))
# 发送⼀些数据到客户端
client_socket.send("thank you !".encode('gbk'))
# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
client_socket.close()