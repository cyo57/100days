random_list = [
    3, 5, 7, 9, 1, 4, 6, 11, 64, 24, 1 ,4
]

def select_sort(items, comp=lambda x, y: x < y):
    '''简单选择排序'''
    # 复制新列表
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


if __name__ == '__main__':
    print(select_sort(random_list))