# 推导式
def a():
    prices = {
        'A': 199,
        'B': 200,
        'C': 185,
        'D': 300
    }
    priceNew = {key: value for key, value in prices.items() if value >= 200}
    print(priceNew)


# 嵌套列表
def b():
    names = ['cyo57', 'hxert', '赵云', '关羽']
    courses = ['语文', '数学', '英语']
    # 录入四名学生 三门课的成绩
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(scores):
            scores[row][col] = float(input(f'输入{name}的{course}成绩: '))


# heapq模块 (堆排序)
# 从列表中找出最大或最小的N个元素
# 解构堆(大根堆/小根堆)
import heapq
def c():
    list1 = [34, 56, 24, 76, 27, 84, 25, 74, 90]
    list2 = [
        {'name': 'A', 'shares': 100, 'price': 90},
        {'name': 'B', 'shares': 200, 'price': 60},
        {'name': 'C', 'shares': 300, 'price': 70}
    ]
    print(heapq.nlargest(100, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(3, list2, key=lambda x: x['price']))


# 迭代工具模块
import itertools
def d():
    # 产生ABCD全排列
    itertools.permutations('ABCD')
    # 产生ABCDE五选三组合
    itertools.combinations('ABCDE', 3)
    # 产生ABCD和123的笛卡尔积
    itertools.product('ABCD', '123')
    # 产生ABC的无限序列循环
    itertools.cycle(('A', 'B', 'C'))

    for _ in itertools.permutations('ABCD'):
        print(_)


# collections模块
from collections import Counter
def e():
    '''常用的类
    namedtuple: 接受类型的名称和属性列表创建一个类
    deque: 
    Counter: dict的子类, 键是元素, 值是元素的计数, 他的most_common()方法可以获取最高频率的元素
    OrderDict: dict的子类, 记录键值对插入的顺序
    defaultdict: 类似字典类型, 但可以通过默认的工行函数获得键对应的默认值
    '''
    words = [
        'apple', 'bag', 'cat', 'dog', 'elephant', 'flag', 'glass', 'happy', 'italy',
        'jack', 'cat', 'lens'
    ]
    counter = Counter(words)
    # 获取前三个最高频率的元素
    print(counter.most_common(3))


if __name__ == '__main__':
    # c()
    # d()
    e()