import socket
import threading
# 发送数据的功能函数
def send_msg(udp_socket):
     # 接收⽤户输⼊的数据
     send_content = input("请输⼊您要发送的数据:")
     # 对数据进⾏gbk编码
     send_data = send_content.encode("gbk")
     # 接收对⽅的ip地址和端⼝号
     dest_ip = input("请输⼊对⽅的ip地址:")
     dest_port = int(input("请输⼊对⽅的端⼝号:"))
     # 发送数据
     udp_socket.sendto(send_data, (dest_ip, dest_port))
# 接收数据的功能函数
def recv_msg(udp_socket):
     while True:
         # 接收数据 1024:表示每次接收数据的最⼤字节数
         recv_data, ip_port = udp_socket.recvfrom(1024)
         # 解码数据
         recv_content = recv_data.decode("gbk")
         print(recv_content, ip_port)
if __name__ == '__main__':
     # 创建udpsocket
     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     # 绑定端⼝， 提示：客户端不强制要求绑定端⼝
     # 在同⼀个电脑上端⼝号不能重复
     udp_socket.bind(("", 8080))
     # 创建接收数据的线程
     recv_thread = threading.Thread(target=recv_msg, args=(udp_socket,))
     # 设置成为守护主线程，主线程退出后⼦线程直接销毁
     recv_thread.setDaemon(True)
     recv_thread.start()
     while True:
         # 接收⽤户的指令
         option = input("请输⼊功能选项 1. 发送 2. 退出:")
         if option == "1":
             # 发送数据
             send_msg(udp_socket)
         elif option == "3":
            break
     # 关闭socket
     udp_socket.close()