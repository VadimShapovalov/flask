# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...] Массив должен быть заполнен случайными целыми числами
# от 1 до 100. При решении задачи нужно использовать асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

import asyncio
import time
import random


async def array_sum(arr: list):
    return sum(arr)


async def main():
    arr = [random.randint(1, 100) for _ in range(10_000_000)]
    print(f'Проверочная сумма элементов массива: {sum(arr)}')
    # start_time = time.time()
    tasks = []
    for i in range(2_000_000, 10_000_001, 2_000_000):
        tasks.append(array_sum(arr[i - 2_000_000:i]))

    start_time = time.time()
    results = await asyncio.gather(*tasks)
    total_sum = sum(results)
    print(f'Время выполнения вычислений: {time.time() - start_time} сек. Результат: {total_sum}')

asyncio.run(main())
