# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...] Массив должен быть заполнен случайными целыми числами
# от 1 до 100. При решении задачи нужно использовать многопроцессорность.
# В каждом решении нужно вывести время выполнения вычислений.

import multiprocessing
import time
import random


def array_sum(arr: list, result):
    result.put(sum(arr))


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(10_000_000)]
    print(f'Проверочная сумма элементов массива: {sum(arr)}')
    processes = []

    result_queue = multiprocessing.Queue()

    for i in range(2_000_000, 10_000_001, 2_000_000):
        p = multiprocessing.Process(target=array_sum, args=(arr[i - 2_000_000:i], result_queue))
        processes.append(p)

    start_time = time.time()

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    results = [result_queue.get() for _ in processes]
    total_sum = sum(results)
    print(f'Время выполнения вычислений: {time.time() - start_time} сек. Результат: {total_sum}')
