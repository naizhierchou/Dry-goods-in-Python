import socket
if __name__ == '__main__':
     # 创建tcp客户端socket
     tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     # 建⽴连接
     tcp_client_socket.connect(("192.168.199.161", 9090))
     # 获取⽤户输⼊⽂件名
     file_name = input("请输⼊您要下载的⽂件名:")
     # 使⽤gbk进⾏编码
     file_name_data = file_name.encode("gbk")
     # 代码执⾏到此，说明连接建⽴成功
     tcp_client_socket.send(file_name_data)
     with open("/home/python/Desktop/" + file_name, "wb") as file:
         # 循环接收服务端发送的⽂件⼆进制数据
         while True:
             # 获取服务端⽂件数据
             file_data = tcp_client_socket.recv(1024)
             if file_data:
                 # 写⼊到指定⽂件
                 file.write(file_data)
             else:
                break
     # 关闭socket
     tcp_client_socket.close()