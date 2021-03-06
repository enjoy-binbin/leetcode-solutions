import asyncio
import time
import threading


# @asyncio.coroutine  # 会把一个生成器标记为coroutine类型
# def hello():
#     print("Hello world! (%s)" % threading.currentThread())

#     # 异步调用asyncio.sleep(2):
#     yield from asyncio.sleep(2)

#     print("Hello again! (%s)" % threading.currentThread())

# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
# 1.把@asyncio.coroutine替换为async；
# 2.把yield from替换为await。
async def hello():
    print("Hello world!")
    r = await asyncio.sleep(2)
    print("Hello again!")


if __name__ == '__main__':
    start = time.time()
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(hello())
    loop.close()
    print('times: %0.4f seconds' % (time.time() - start))
