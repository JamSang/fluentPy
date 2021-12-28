def func4key(x):
    rs = x%2
    # print(rs)
    return rs

def main():
    s = list(range(10))
    print(s)

    print(s.sort())
    print(s)

    print(s.sort(reverse=True))
    print(s)

    print(sorted(s))
    ns = sorted(s,key=func4key,reverse=True)
    print(ns)
    s.sort(key=lambda x:x%2,reverse=True)
    print(s)

if __name__ == '__main__':
    main()
