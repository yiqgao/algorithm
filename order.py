import time


def output(types):
    def method(func):
        def wrapper(*args, **kwargs):
            handle_dataset = func(*args, **kwargs)
            print('运行时间为{duration}'.format(duration=time.process_time()))
            print('使用{type}算法的结果为:{result}'.format(
                result=handle_dataset, type=types))
        return wrapper
    return method


class OrderFunc:
    def __init__(self, dataset):
        self.dataset = dataset

    @output('冒泡排序')
    # 从头开始，两两比较，将大的数字移动到后面，第一轮将把最大的数排到最后，第二轮将次大的数排到倒数第二位，以此类推
    def bubble_sort(self):
        handle_dataset = self.dataset[:]
        total_length = len(handle_dataset) - 1
        j = 0
        while j < total_length:
            i = 0
            not_change_flag = True  # 某个循环内没有替换元素
            while i < total_length - j:
                if handle_dataset[i] > handle_dataset[i+1]:
                    exchange_temp = handle_dataset[i]
                    handle_dataset[i] = handle_dataset[i+1]
                    handle_dataset[i+1] = exchange_temp
                    not_change_flag = False
                i = i+1
            if not_change_flag:
                print('本次冒泡循环次数:{count}'.format(count=j))
                break
            j = j+1
        return handle_dataset


p = OrderFunc([23, 65, 13, 45, 24, 17, 19, 33, 76, 35, 54, 33,
               55, 45, 42, 11, 234, 567, 345, 987, 343, 2, 56, 114, 32])
p.bubble_sort()
