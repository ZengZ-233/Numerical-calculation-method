import time

from sympy import *
import matplotlib.pyplot as plt


def f(x):
    f = x * exp(x) - 1
    return f


def single_secant(x0, x1):
    x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    return x2


def double_secant(x1, x2):
    x3 = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
    return x3


if __name__ == '__main__':
    x_single = []
    y_single = []
    l_single = []
    x1 = 0.5
    x2 = 0.6
    continue_ = 1
    i = 0
    t1=time.time()
    """单点弦法"""
    while continue_:
        x3 = single_secant(x1, x2)
        x2 = x3
        l_single.append(x3)
        if len(l_single) > 1:
            i += 1
            error = abs(l_single[-1] - l_single[-2])
            x_single.append(i)
            y_single.append(error)
            if error <1e-7 :
                continue_ = 0
        else:
            pass
    # """双点弦法"""
    # while continue_:
    #     x3 = single_secant(x1, x2)
    #     x1 = x2
    #     x2 = x3
    #     i += 1
    #     l_single.append(x3)
    #     if len(l_single) > 1:
    #         error = abs(l_single[-1] - l_single[-2])
    #         x_single.append(i)
    #         y_single.append(error)
    #         if error == 0:
    #             continue_ = 0
    t2=time.time()
    print("时长:",t2-t1)
    print("迭代次数:",len(l_single))
    print(f'所求方程式的根为{l_single[-1]}')
    # 设置绘图风格
    plt.style.use('ggplot')
    # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 坐标轴负号的处理
    plt.rcParams['axes.unicode_minus'] = False
    # 横坐标是迭代次数
    # 纵坐标是误差值
    plt.plot(x_single,
             y_single,
             color='steelblue',  # 折线颜色
             marker='o',  # 折线图中添加圆点
             markersize=3,  # 点的大小
             )
    # 修改x轴和y轴标签
    plt.xlabel('迭代次数')
    plt.ylabel('误差值')
    # 显示图形
    plt.show()
