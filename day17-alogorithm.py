'''
常用算法
1.
公鸡5元一只, 母鸡3元一只, 小鸡1元三只
100元买100只鸡, 小鸡公鸡共多少只

2.
A, B, C, D, E  合伙抓鱼
di'er'tian
'''


def exhaustive():
    '''穷举法'''
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if x * 5 + y * 3 + z//3 == 100 and z % 3 == 0:
                print('%s公鸡, %s母鸡, %s小鸡' % (x, y, z))


if __name__ == '__main__':
    exhaustive()
