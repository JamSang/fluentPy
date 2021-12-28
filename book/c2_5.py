"""
对序列使用+和*
"""
import dis


def main():
    t = [1, 2, 3]
    a = [t * 3]
    print(a)

    my_list = [[]] * 3
    print(my_list)
    print(id(my_list[0]))
    print(id(my_list[1]))
    print(id(my_list[2]))

    my_list[0].append(1)
    print(my_list)


def checkerboard():
    # 正确写法
    board = [['_'] * 3 for i in range(3)]
    # 错误写法
    board = [['_'] * 3] * 3

    print(board)
    board[1][2] = 'x'
    print(board)



def augmented_assignment():
    # 增量赋值

    l = [1,2,3]
    print(id(l))
    l *= 3
    print(id(l))

    t = (1,2,3)
    print(id(t))
    t *= 3
    print(id(t))


if __name__ == '__main__':
    main()
    checkerboard()
    augmented_assignment()
    dis.dis('s[a] += b')
