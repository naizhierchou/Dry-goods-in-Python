import socket
import os
if __name__ == '__main__':
     # 创建tcp服务端socket
     tcp_serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     # 设置socket选项，防⽌程序退出端⼝不⽴即释放的问题
     tcp_serve_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
     # 绑定端⼝
     tcp_serve_socket.bind(("", 9090))
     # 设置监听，把主动套接字改成被动套接字，被动套接字只能接收客户端的连接请求，不能收发消息
     tcp_serve_socket.listen(128)
     # 循环接收客户端的连接请求， 提示：现在的下载是同步下载，⼀个⽤户下载完成以后另外⼀个⽤户才能下载
     while True:
         # 接收客户端的连接请求
         service_client_socket, ip_port = tcp_serve_socket.accept()
         # 代码执⾏到说明解阻塞，说明连接建⽴成功
         file_name_data = service_client_socket.recv(1024)
         # 解码数据
         file_name = file_name_data.decode("gbk")
         print(file_name, ip_port)
         if os.path.exists(file_name):
             # ⽂件存在
             with open(file_name, "rb") as file:
                 # 读取⽂件数据
                 while True:
                     file_data = file.read(1024)
                     if file_data:
                         # 发送⽂件数据给客户端
                        service_client_socket.send(file_data)
                     else:
                        break
         else:
            print("⽂件不存在")
         # 终⽌和客户端服务
         service_client_socket.close()
     # 终⽌提供处理连接请的服务
     tcp_serve_socket.close()