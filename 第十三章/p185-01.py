#coding=utf-8
from socket import *
# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 2. 绑定本地的相关信息，如果⼀个⽹络程序不绑定，则系统会随机分配
local_addr = ('', 7788) # ip地址和端⼝号，ip⼀般不⽤写，表示本机的任何⼀个ip
udp_socket.bind(local_addr)
# 3. 等待接收对⽅发送的数据
recv_data = udp_socket.recvfrom(1024) # 1024表示本次接收的最⼤字节数
# 4. 显示接收到的数据
print(recv_data[0].decode('gbk'))
# 5. 关闭套接字
udp_socket.close()