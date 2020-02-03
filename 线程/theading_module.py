import threading
import time


# 运行此程序
def run(count):
    for count in range(10):
        print(threading.current_thread().name)
        time.sleep(1)


thread_list = []
for i in range(20):
    t = threading.Thread(target=run, args=(i, ))  # 线程创建
    t.start()   # 线程运行
    thread_list.append(t)   # 加入线程列表


for i in thread_list:

    # 阻塞，等它们运行结束
    i.join()
