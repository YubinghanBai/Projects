import threading
import time

def count_down(name, delay):
    print(f"{name} started")
    while delay > 0:
        print(f"{name}: {delay}")
        time.sleep(1)
        delay -= 1
    print(f"{name} finished")

# 创建两个线程
thread1 = threading.Thread(target=count_down, args=("Thread 1", 5))
thread2 = threading.Thread(target=count_down, args=("Thread 2", 3))
thread1.setDaemon(True)
# 启动线程
thread1.start()
thread2.start()

# 等待线程结束
thread1.join()
thread2.join()

print("All threads finished")

#<p><a href="//wx3.moyu.im/large/6d050af1ly1hpv7464t9mj20ku0ku76w.jpg" target="_blank" class="view_img_link">[查看原图]</a><br><img src="//wx3.moyu.im/mw600/6d050af1ly1hpv7464t9mj20ku0ku76w.jpg" style="max-width: 100%; max-height: 450px;"></p>
