def unpacking_tuple():
    date = (2022, '01', 31)
    print('%s-%s-%s' % date)

    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates
    print(latitude, longitude)

    a, b = (1, 2)
    b, a = a, b
    print(a, b)

    import os
    path, filename = os.path.split('/home/jam/test.py')
    print(path)
    print(filename)
    _, filename = os.path.split('/home/jam/test.py')


def printTuple(*args):
    print(args)


def unpacking():
    a, b, *s = range(5)
    print(a, b, s)
    a, b, *s = range(3)
    print(a, b, s)
    a, b, *s = range(2)
    print(a, b, s)
    a, *b, s = range(5)
    print(a, b, s)


# 嵌套元组拆包
def unpackingNestTuple():
    # (城市,国家,xx,(坐标))
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:^9.4} | {:^9.4f}'
    for name, _, _, (latitude, longitude) in metro_areas:
        print(fmt.format(name, latitude, longitude))


def tupleHasName():
    import collections
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    # 这是个class  Card类
    print(Card)
    from collections import namedtuple
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)
    print(tokyo.coordinates)
    print(tokyo[0])

    jam = namedtuple('Student', 'name age sex')('jam', 24, 'boy')
    shooting = namedtuple('Student', ['name', 'age', 'sex'])('shooting', 24, 'girl')
    print(jam)
    print(shooting)
    print(type(jam), type(shooting))


def attribute4Tuple():
    from collections import namedtuple
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    #  _fields 属性是一个包含这个类所有字段名称的元组
    print(City._fields)

    delhi_data = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
    # _make 作用同 City(*delhi_data),接受一个可迭代对象来生成这个类的一个实例
    delhi = City._make(delhi_data)

    # _asdict 具名元组以 collections.OrderedDict 的形式返回
    print(delhi._asdict())


if __name__ == '__main__':
    unpacking_tuple()
    unpacking()
    printTuple()
    printTuple(1, 2, 3)
    unpackingNestTuple()
    tupleHasName()
    attribute4Tuple()
