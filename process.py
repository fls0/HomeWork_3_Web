import time

from multiprocessing import Process, current_process, cpu_count, Pool
from functools import wraps


def timing_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"Функція '{func.__name__}' виконана за {execution_time:.4f} секунд")
        return result
    return wrapper


@timing_dec
def factorize(numbers):
    result = []
    for num in numbers:
        for i in range(1, num + 1):
            if num % i == 0:
                result.append(i)
    return result
@timing_dec
def factorize_for_pool(num):
    print(current_process().name)
    result = [1]
    for i in range(2, num+1):
        if not num % i:
            result.append(i)
    return result

@timing_dec
def pool_factorize(numbers):
    with Pool(cpu_count()) as pool:
        pool.map(factorize_for_pool, numbers)
        pool.close()
        pool.join()


if __name__ == '__main__':
    a = factorize([128, 255, 99999, 10651060])

    print(f"Count CPU: {cpu_count()}")

    pool_factorize([128, 255, 99999, 10651060])

    assert a == [1, 2, 4, 8, 16, 32, 64, 128, 1, 3, 5, 15, 17, 51, 85, 255, 1, 3, 9, 41, 123, 271, 369, 813,
                 2439, 11111, 33333, 99999, 1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
