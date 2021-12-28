import collections


def listcomps():
    codes = [ord(s) for s in symbols]
    print(codes)


def filterAndMap():
    # map/filter 组合 并不 比列表推导快
    codes_1 = [ord(s) for s in symbols if ord(s) > 127]
    codes_2 = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(codes_1)
    print(codes_2)


def cartesian():
    # 笛卡尔乘积
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tShirts = [(c, s)
               for c in colors
               for s in sizes]
    print(tShirts)


def generator_expression():
    t = tuple(ord(s) for s in symbols)
    print(t)

    import array
    arr = array.array('I', (ord(s) for s in symbols))
    print(arr)

    # 生产器表达式
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']

    # 先生成列表, 在遍历
    for tshirt in [f'{c},{s}' for c in colors for s in sizes]:
        print(tshirt)
    # 生成一个,处理完, 再迭代下一个
    for tshirt in (f'{c},{s}' for c in colors for s in sizes):
        print(tshirt)




if __name__ == '__main__':
    symbols = '@#$%^&*$¢£$¥€¤%'
    listcomps()
    filterAndMap()
    cartesian()
    generator_expression()
