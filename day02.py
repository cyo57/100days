'''
1.华氏温度转换摄氏温度
C=(F-32)/1.8

2.圆半径计算周长和面积

3.判断年份是不是闰年
'''

def tempConversion():
    '''
    温度转换, 华氏->摄氏
    '''

    f = float(input('华氏温度:'))
    c = (f-32)/1.8

    print('%.2f华氏度转换后为: %.2f摄氏度' % (f,c))

def circle_cul():
    '''
    圆半径计算r和s
    '''
    from math import pi

    r = float(input('圆半径:'))
    area = pi * r * r
    perimeter = pi * 2 * r

    print('%s半径的圆周长为：%.2f, 面积为: %.2f' % (r, perimeter, area))

def isLeapYear():
    year = int(input('输入年份:'))
    is_leap = year % 4 == 0 \
        and year % 100 != 0 \
        or year % 400 == 0
    print(is_leap)

if __name__ == '__main__':
    #tempConversion()
    #circle_cul()
    isLeapYear()