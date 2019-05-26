import gevent
import urllib.request # ⽹络请求模块
from gevent import monkey
# 打补丁： 让gevent使⽤⽹络请求的耗时操作，让协程⾃动切换执⾏对应的下载任务
monkey.patch_all()
# 根据图⽚地址下载对应的图⽚
def download_img(img_url, img_name):
     try:
         print(img_url)
         # 根据图⽚地址打开⽹络资源数据
         response = urllib.request.urlopen(img_url)
         # 创建⽂件把数据写⼊到指定⽂件⾥⾯
         with open(img_name, "wb") as img_file:
             while True:
                 # 读取⽹络图⽚数据
                 img_data = response.read(1024)
                 if img_data:
                     # 把数据写⼊到指定⽂件⾥⾯
                     img_file.write(img_data)
                 else:
                    break
     except Exception as e:
        print("图⽚下载异常:", e)
     else:
        print("图⽚下载成功: %s" % img_name)
if __name__ == '__main__':
     # 准备图⽚地址
     img_url1 ="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=551346117,2593226454&fm=27&gp=0.jpg"
     img_url2 ="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=829730016,3409799239&fm=27&gp=0.jpg"
     img_url3 ="https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1815077192,817368579&fm=27&gp=0.jpg"
     # 创建协程指派对应的任务
     g1 = gevent.spawn(download_img, img_url1, "1.jpg")
     g2 = gevent.spawn(download_img, img_url2, "2.jpg")
     g3 = gevent.spawn(download_img, img_url3, "3.jpg")
     # 主线程等待所有的协程执⾏完成以后程序再退出
     gevent.joinall([g1, g2, g3])