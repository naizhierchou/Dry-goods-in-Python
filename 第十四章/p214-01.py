import socket
# 创建tcp socket
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ⽬的信息
server_ip = input("请输⼊服务器ip:")
server_port = int(input("请输⼊服务器port:"))
# 链接服务器
tcp_client_socket.connect((server_ip, server_port))
# 提示⽤户输⼊数据
send_data = input("请输⼊要发送的数据：")
tcp_client_socket.send(send_data.encode("gbk"))
# 接收对⽅发送过来的数据，最⼤接收1024个字节
recvData = tcp_client_socket.recv(1024)
print('接收到的数据为:', recvData.decode('gbk'))
# 关闭套接字
tcp_client_socket.close()