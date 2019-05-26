import socket
# 1. 创建udp套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2. 准备接收⽅的地址
dest_addr = ('192.168.236.129', 8080)
# 3. 从键盘获取数据
send_data = input("请输⼊要发送的数据:")
# 4. 发送数据到指定的电脑上
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
# 5. 等待接收对⽅发送的数据
recv_data = udp_socket.recvfrom(1024) # 1024表示本次接收的最⼤字节数
# 6. 显示对⽅发送的数据
# 接收到的数据recv_data是⼀个元组
# 第1个元素是对⽅发送的数据
# 第2个元素是对⽅的ip和端⼝
print(recv_data[0].decode('gbk'))
print(recv_data[1])
# 7. 关闭套接字
udp_socket.close()
