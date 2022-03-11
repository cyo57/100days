random_list = [
    3, 5, 37, 9, 1, 2, 4, 8
]

def select_sort(items, comp=lambda x, y: x < y):
    #count = 0
    '''简单选择排序'''
    # 复制新列表
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            #count += 1 #统计比对次数
            if comp(items[j], items[min_index]):
                min_index = j
            print(items[j], items[min_index], min_index)
            print(items, '\n')
        items[i], items[min_index] = items[min_index], items[i]
    #print('count: %s' % count)
    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    '''冒泡排序'''
    #count = 0
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1): # (-1 -i)
            #count += 1 #统计比对次数
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    #print('count: %s' % count)
    return items


def bubble_sort_pro(items, comp=lambda x, y:x > y):
    '''搅拌排序 (冒泡+)'''
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
            if swapped:
                swapped = False
                for j in range(len(items) - 2 - i, i, -1):
                    if comp(items[j - 1], items[j]):
                        items[j], items[j - 1] = items[j - 1], items[j]


if __name__ == '__main__':
    print(select_sort(random_list))
    #print(bubble_sort(random_list))