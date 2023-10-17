import time
import math


def f(x):
    return math.exp(-x)


def easy_iteration(x):
    x_next = math.exp(-x)
    while abs(abs(x) - abs(x_next)) > 0.000000000000001:
        x = x_next
        x_next = math.exp(-x)
    print(x, x_next)
    print('\n')


def get_speed_0(x):
    x_next = (math.exp(-x) + 0.6 * x) / 1.6
    while abs(abs(x) - abs(x_next)) > 0.000000000000001:
        x = x_next
        x_next = (math.exp(-x) + 0.6 * x) / 1.6
    print(x, x_next)
    print('\n')


def get_speed_1(x):
    x1 = f(x)
    x2 = f(x1)
    x3 = x2 - ((x2 - x1) ** 2) / (x2 - 2 * x1 + x)
    while abs(abs(x3) - abs(x)) > 0.000000000000001:
        x = x3
        x1 = f(x)
        x2 = f(x1)
        x3 = x2 - ((x2 - x1) ** 2) / (x2 - 2 * x1 + x)
    print(x, x3)
    print('\n')


if __name__ == '__main__':
    t0 = time.time()
    print('简单迭代法:')
    easy_iteration(x=0)
    t1 = time.time()
    print("简单迭代法的时间:", t1 - t0)

    t2 = time.time()
    print('普通加速迭代法:')
    get_speed_0(x=0)
    t3 = time.time()
    print("简单迭代法的时间:", t3 - t2)

    t4 = time.time()
    print('埃特金加速迭代法:')
    get_speed_1(x=0)
    t5 = time.time()
    print("简单迭代法的时间:", t5 - t4)
