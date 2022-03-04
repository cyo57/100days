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
import heapq
def c():
    list1 = [34, 56, 24, 76, 27, 84, 25, 74, 90]
    print(heapq.nlargest(100, list1))


if __name__ == '__main__':
    c()