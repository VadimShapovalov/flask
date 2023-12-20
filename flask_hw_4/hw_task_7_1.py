# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...] Массив должен быть заполнен случайными целыми числами
# от 1 до 100. При решении задачи нужно использовать многопоточность.
# В каждом решении нужно вывести время выполнения вычислений.

import time
import threading
import random


def array_sum(arr: list, result: list):
    result.append(sum(arr))


threads = []
results = []

arr = [random.randint(1, 100) for _ in range(10_000_000)]
print(f'Проверочная сумма элементов массива: {sum(arr)}')

for i in range(2_000_000, 10_000_001, 2_000_000):
    t = threading.Thread(target=array_sum, args=(arr[i - 2_000_000:i], results))
    threads.append(t)

start_time = time.time()

for t in threads:
    t.start()
for t in threads:
    t.join()

total_sum = sum(results)
print(f'Время выполнения вычислений: {time.time() - start_time} сек. Результат: {total_sum}')
