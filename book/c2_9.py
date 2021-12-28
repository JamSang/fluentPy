from array import array


from random import random

def save_load():
    floats = array('d', (random() for i in range(10 ** 7)))
    print(floats[-1])
    with open('floats.bin', 'wb') as fp:
        floats.tofile(fp)

    floats_2 = array('d')
    with open('floats.bin', 'rb') as fp:
        floats_2.fromfile(fp, 10 ** 7)

    print(floats_2[-1])
    print(floats[555] == floats_2[555])


def memory_view():
    # 类型码'h'
    numbers = array('h', [-2, -1, 0, 1, 2])
    # [-2, -1, 0, 1, 2]
    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0])

    # 把 memv 里的内容转换成'B'类型, 无符号字符
    memv_oct = memv.cast('B')
    memv_oct.tolist()
    # [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
    print(memv_oct)
    memv_oct[5] = 4

    print(numbers)

def numpy_scipy():
    import numpy
    import scipy

def collections_deque():
    '''
    双向队列
    :return:
    '''
    from collections import deque
    # maxlen 可选参数, 队列可容纳元素数量, 设定后不可更改
    dq = deque(range(10),maxlen=10)
    print(dq)

    # rotate n>0 右移, n<0 左移
    dq.rotate(3)
    print(dq)

    dq.rotate(-5)
    print(dq)

    # 满队添加 会挤掉元素
    dq.append(11)
    print(dq)
    dq.appendleft(99)
    print(dq)
    dq.extend([99,88,77])
    print(dq)
    dq.extendleft([55,44])
    print(dq)

def other_queue():
    from queue import Queue,LifoQueue,PriorityQueue
    # 不同的线程可以利用这些数据类型来交换信息
    qq = Queue(maxsize=5)
    lq = LifoQueue(maxsize=6)
    pq = PriorityQueue(maxsize=7)
    # 满队列后,不会丢弃旧值, 锁住,等待移出

    import multiprocessing
    mq = multiprocessing.Queue(maxsize=20)
    # 同queue.Queue类似, 给进程间通信用的

    jq = multiprocessing.JoinableQueue(maxsize=8)
    # 任务管理使用






if __name__ == '__main__':
    # save_load()
    # memory_view()
    # numpy_scipy()
    collections_deque()


