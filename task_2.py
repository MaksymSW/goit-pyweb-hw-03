"""
Друга частина для процесів
Напишіть реалізацію функції factorize, яка приймає список чисел та повертає список чисел,
на які числа з вхідного списку поділяються без залишку.
Реалізуйте синхронну версію та виміряйте час виконання.
Потім покращіть продуктивність вашої функції, реалізувавши використання кількох ядер процесора
для паралельних обчислень і замірьте час виконання знову.
Для визначення кількості ядер на машині використовуйте функцію cpu_count() з пакета multiprocessing
Для перевірки правильності роботи алгоритму самої функції можете скористатися тестом:

def factorize(*number):
        # YOUR CODE HERE
        raise NotImplementedError() # Remove after implementation


    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790,
    1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
"""
from time import time
from multiprocessing import Pool, cpu_count

def factorize(*number):
    total_list = []
    for i in number:
        local_list = []
        for j in range(1, i+1):
            if i % j == 0:
                local_list.append(j)
        total_list.append(local_list)
    return total_list

if __name__ == '__main__':
    cpu = cpu_count()
    print(f'Количество ядер: {cpu}\n')

    factorize_list = (128, 255, 99999, 10651060)

    start_time = time()
    a, b, c, d  = factorize(128, 255, 99999, 10651060)
    end_time = time()
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    
    

    print (f'Синхронний час: {end_time - start_time}\n')

    start_time = time()
    with Pool(processes=cpu) as pool:
        result = pool.map(factorize,factorize_list )
    end_time = time()
    print (f'Асинхронний час: {end_time - start_time}\n')




