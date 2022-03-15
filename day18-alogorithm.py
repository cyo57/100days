'''
常用算法

题目请查看markdown.md
'''


def exhaustive_a():
    '''穷举法'''
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if x * 5 + y * 3 + z//3 == 100 and z % 3 == 0:
                print('%s公鸡, %s母鸡, %s小鸡' % (x, y, z))


def exhaustive_b():
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5


def greedy_a():
    class Thing(object):
        '''物品'''

        def __init__(self, name, price, weight):
            self.name = name
            self.weight = weight
            self.price = price

        @property
        def value(self):
            '''性价比'''
            return self.price / self.weight

    def input_thing():
        name_str, price_str, weight_str = input('名字 价格 重量:').split()
        return name_str, int(price_str), int(weight_str)

    def main():
        max_weight, num_of_things = map(int, input('背包重量容量 可用物品件数:').split())
        all_things = []
        for _ in range(num_of_things):
            all_things.append(Thing(*input_thing()))  # 带*会翻译成元组
        all_things.sort(key=lambda x: x.value, reverse=True)
        total_weight = 0
        total_price = 0
        for thing in all_things:
            if total_weight + thing.weight <= max_weight:
                print(f'小偷拿走了{thing.name} 性价比{thing.value}')
                total_weight += thing.weight
                total_price += thing.price
        print(f'总价值{total_price}元, 重{total_weight}')

    main()


if __name__ == '__main__':
    # exhaustive_b()
    greedy_a()
