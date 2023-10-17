import time
from sympy import *
import matplotlib.pyplot as plt

x = symbols('x')
x0 = 1.5
x_list = [x0]
x_values = []
y_values = []
i = 0


def f(x):
    f = x * exp(x) - 1
    return f

l_w = []
t1 = time.time()
w = 4
while True:
    if f(x) == 0:
        print('极值点：', x0)
        break
    else:
        x0 = x0 -  w*f(x0) / diff(f(x), x).subs(x, x0)
        x_list.append(x0)
        l_w.append(w)
        w *= 0.5

    if len(x_list) > 1:
        i += 1
        error = abs((x_list[-1] - x_list[-2]) / x_list[-1])
        x_values.append(i)
        y_values.append(error)
        if error == 0:
            print(f'迭代第{i}次后，误差为0')
            break
    else:
        pass
t2 = time.time()
print("时长:", t2 - t1)
print("迭代权重个数:", len(l_w))
for i in range(len(l_w)):
    print("迭代权重值:", l_w[i])
print(f'所求方程式的根为{x_list[-1]}')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x_values,
         y_values,
         color='green',
         marker='o',
         markersize=3,
         )
plt.xlabel('迭代次数')
plt.ylabel('误差值')
plt.show()
