import time


def output(types):
    def method(func):
        def wrapper(*args, **kwargs):
            handle_dataset = func(*args, **kwargs)
            print('使用{type}算法的结果为:{result}'.format(
                result=handle_dataset, type=types))
            print('运行时间为{duration}'.format(duration=time.process_time()))
        return wrapper
    return method


class OrderFunc:
    def __init__(self, dataset):
        self.dataset = dataset

    @output('冒泡排序')
    def bubble_sort(self):
        handle_dataset = self.dataset[:]
        total_length = len(handle_dataset) - 1
        j = 0
        while j < total_length:
            i = 0
            while i < total_length - j:
                if handle_dataset[i] > handle_dataset[i+1]:
                    exchange_temp = handle_dataset[i]
                    handle_dataset[i] = handle_dataset[i+1]
                    handle_dataset[i+1] = exchange_temp
                i = i+1
            j = j+1
        return handle_dataset


p = OrderFunc([23, 65, 13, 45, 24, 17, 19, 33, 76, 35, 54, 33,
               55, 45, 42, 11, 234, 567, 345, 987, 343, 2, 56, 114, 32])
p.bubble_sort()
