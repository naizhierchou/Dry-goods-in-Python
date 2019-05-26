import socket
# 1. 创建udp套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2. 准备接收⽅的地址
# '192.168.1.103'表示⽬的ip地址
# 8080表示⽬的端⼝
dest_addr = ('192.168.1.103', 8080) # 注意 是元组，ip是字符串，端⼝是数字
# 3. 从键盘获取数据
send_data = input("请输⼊要发送的数据:")
# 4. 发送数据到指定的电脑上的指定程序中
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
# 5. 关闭套接字
udp_socket.close()