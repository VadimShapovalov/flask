# Решение задачи стандартным способом.

import time
import random


def array_sum(arr: list):
    return sum(arr)


arr = [random.randint(1, 100) for _ in range(10_000_000)]

start_time = time.time()
my_sum = array_sum(arr)
print(f'Время выполнения вычислений: {time.time() - start_time} сек. Результат: {my_sum}')
