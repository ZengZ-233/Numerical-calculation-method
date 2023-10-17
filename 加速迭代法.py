import time
import math


def f(x):
    return math.exp(-x)


def get_speed_1(x):
    x1 = f(x)
    x2 = f(x1)
    x3 = x2 - ((x2 - x1) ** 2) / (x2 - 2 * x1 + x)
    while abs(abs(x3) - abs(x)) > 0.000000000000001:
        x = x3
        x1 = f(x)
        x2 = f(x1)
        if abs(x2 - 2 * x1 + x) < 1e-10:
            # 处理分母为零的情况，可以选择一个新的初始值或采取其他措施
            break
        else:
            x3 = x2 - ((x2 - x1) ** 2) / (x2 - 2 * x1 + x)
    print(x, x3)
    print('\n')


if __name__ == '__main__':
    t4 = time.time()
    print('埃特金加速迭代法:')
    get_speed_1(x=0)
    t5 = time.time()
    print("简单迭代法的时间:", t5 - t4)
