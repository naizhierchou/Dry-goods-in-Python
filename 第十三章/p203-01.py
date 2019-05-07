import socket
# 创建udp的套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ...这⾥是使⽤套接字的功能（省略）...
# 不⽤的时候，关闭套接字
s.close()