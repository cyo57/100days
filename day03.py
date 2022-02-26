'''
1. 厘米和米的转换

2. 分数评级
70-80:C, 80-90:B, 90-100:A

3. 三条边长计算周长面积
海伦: area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
'''

def unitConvert():
    '''
    cm和m转换
    '''
    now_unit = input('单位(cm/m):')
    now_num = float(input('数值(%s):' % now_unit))

    if now_unit == ('cm' or '厘米'):
        convert_num = now_num/100
        print('%scm = %sm' % (now_num, convert_num))
    if now_unit == ('m' or '米'):
        convert_num = now_num * 100
        print('%scm = %sm' % (now_num, convert_num))

def scoreLevel():
    score = float(input('分数: '))
    if score < 70:
        print('D')
    elif score < 80:
        print('C')
    elif score < 90:
        print('B')
    else:
        print('A')

def triangle_cal():
    a = float(input('A边长:'))
    b = float(input('B边长:'))
    c = float(input('C边长:'))
    if (a + b) > c \
        and (a + c) > b \
        and (b + c) > a:
        perimeter = a + b + c
        p = perimeter/2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('边长:%.2f, 面积:%.2f' % (perimeter, area))
    else:
        print('非三角形')

if __name__ == '__main__':
    #unitConvert()
    #scoreLevel()
    triangle_cal()