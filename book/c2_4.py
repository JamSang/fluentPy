"""
切片

"""


def main():
    # slice 切片对象
    a = slice(0, 99, 6)
    print(a, type(a))
    s = [i for i in range(100)]
    print(s[a])

    ss = [[x + y for x in range(10)] for y in range(10)]
    print(ss)
    # 原生二维不可以
    # print(ss[0:3,6:9])

    # 未验证
    # import NumPy as np
    # np.ndarray(ss)
    # print(ss[0:3,6:9])

    # 省略 ellipsis  ...  Ellipsis 对象的别名,  Ellipsis 对象又是 ellipsis 类的单一实例
    # import NumPy as np
    print(s[1:...])
    # ellipsis 是类名， 全小写， 而它的内置实例写作 Ellipsis。
    # 其实跟 bool 是小写， 但是它的两个实例写作 True 和 False 异曲同工。


def test():
    l = list(range(50))
    print(l)
    l[2:5] = [200, 300]
    print(l)

    del l[10:16]
    print(l)

    print(l[20::3])
    # 数量相等才行 右侧可迭代
    l[20::3] = list(range(len(l[20::3])))
    print(l)

    l[20:25] = [100]
    print(l)


if __name__ == '__main__':
    # main()
    test()
