import threading
import time
def task():
     time.sleep(1)
     print("当前线程:", threading.current_thread().name)
if __name__ == '__main__':
    for _ in range(5):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()