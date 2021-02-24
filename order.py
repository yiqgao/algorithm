import time


def output(types):
    def method(func):
        def wrapper(*args, **kwargs):
            handle_dataset, total_calculate_count = func(*args, **kwargs)
            print('使用\033[1;35m{type}\033[0m算法的运行时间为\033[1;35m{duration}\033[0m,计算总次数为\033[1;35m{cal_count}\033[0m\n'.format(
                duration=time.process_time(), cal_count=total_calculate_count, type=types))
            print('结果为:{result}'.format(
                result=handle_dataset))
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
        total_calculate_count = 0
        period = 0
        while period < total_length:
            i = 0
            not_change_flag = True  # 某个循环内没有替换元素
            while i < total_length - period:
                if handle_dataset[i] > handle_dataset[i+1]:
                    exchange_temp = handle_dataset[i]
                    handle_dataset[i] = handle_dataset[i+1]
                    handle_dataset[i+1] = exchange_temp
                    not_change_flag = False
                i = i+1
                total_calculate_count = total_calculate_count + 1
            if not_change_flag:
                break
            period = period+1
        return handle_dataset, total_calculate_count

    @output('选择排序')
    def selection_sort(self):
        handle_dataset = self.dataset[:]
        total_length = len(handle_dataset) - 1
        total_calculate_count = 0
        period = 0
        while period < total_length:
            i = 0
            max_num = handle_dataset[0]
            max_i = 0
            while i <= total_length - period:
                if handle_dataset[i] > max_num:
                    max_num = handle_dataset[i]
                    max_i = i
                i = i+1
                total_calculate_count = total_calculate_count+1
            handle_dataset[max_i] = handle_dataset[total_length - period]
            handle_dataset[total_length - period] = max_num
            period = period + 1
        return handle_dataset, total_calculate_count


if __name__ == '__main__':
    import random
    sample_data = [random.randint(0,300) for x in range(100)]
    p = OrderFunc(sample_data)
    print("\n原始数据为  {list}\n".format(list=sample_data))
    for item in dir(p):
        if callable(getattr(p, item)) and item.find('__') == -1:
            print('-'*50)
            eval('p.'+item+'()')
