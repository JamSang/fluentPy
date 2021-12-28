from array import array
from random import random

if __name__ == '__main__':
    floats = array('d', (random() for i in range(10 ** 7)))
    print(floats[-1])
    with open('floats.bin', 'wb') as fp:
        floats.tofile(fp)

    floats_2 = array('d')
    with open('floats.bin', 'rb') as fp:
        floats_2.fromfile(fp, 10 ** 7)

    print(floats_2[-1])
    print(floats[555] == floats_2[555])
