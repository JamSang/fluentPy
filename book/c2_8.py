import bisect

"""
用bisect来搜索
bisect(haystack, needle) 在haystack（干草垛）里搜索needle（针）的位置
该位置满足的条件是，把  needle 插入这个位置之后， haystack还能保持升序
haystack 必须有序 
"""


NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'


def func_1():
    pass


if __name__ == '__main__':
    HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    print(bisect.bisect_left(HAYSTACK, 17))
    print(bisect.bisect_right(HAYSTACK, 17))
    HAYSTACK.insert(bisect.bisect(HAYSTACK, 17), 17)
    print(HAYSTACK)

    bisect.insort(HAYSTACK,19)
    print(HAYSTACK)