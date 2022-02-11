'''
1. 判断正整数是否为素数
即仅能被1或自身整除的数

2. 两个正整数的最大公约数和最小公倍数

3. 打印如下图形
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
'''

def isPrime():
    is_prime = True
    num = int(input('正整数:'))
    for i in range(2, int(num/2)):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)

def num():
    a = int(input('正整数a: '))
    b = int(input('正整数b: '))
    if a > b:
        a,b = b,a
    for i in range(a, 1, -1):
        if a%i == 0 and b%i == 0:
            print('公约数是%d' % i)
            print('公倍数是%d' % a*b//i)
            break


#isPrime()
num()