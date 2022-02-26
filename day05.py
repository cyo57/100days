'''
1. 斐波那契数列
'''


def fibonacciSequence():
    a = 1
    b = 1
    count = 0
    print(a)
    print(b)
    while(count != 10):
        a += b
        print(a)
        b += a
        print(b)
        count+=1

fibonacciSequence()