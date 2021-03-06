import time
import threading

# 我有0块钱
money = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，最后结果应该是为0
    global money  # 声明全局变量
    money = money + n
    money = money - n


# 线程执行的函数
def run_thread(n):
    for i in range(100000):
        lock.acquire()  # 加锁
        try:
            change_it(n)
        finally:
            lock.release()  # 最后记得要释放锁


if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(money)
