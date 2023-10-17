import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
xl = -100
xr = 100


def f(x):
    f = x ** 3 - x - 1  # 需要求根的函数
    return f


xm_list = []
x_values = []
y_values = []
m = 0
while True:
    xm = (xl + xr) / 2
    xm_list.append(xm)
    m += 1
    if f(xm) == 0:
        break
    else:
        pass
    if f(xl) * f(xm) < 0:
        xl = xl
        xr = xm
    elif f(xl) * f(xm) > 0:
        xl = xm
        xr = xr
    else:
        break
    if len(xm_list) > 1:
        error = abs((xm_list[-1] - xm_list[-2]) / xm_list[-1])
        x_values.append(m)
        y_values.append(error)
        if error == 0:
            break
    else:
        pass
print(f'xl={xl},xr={xr}')
print(f'迭代第{m}次后，误差为0,得到方程的根为：{(xl + xr) / 2}')

plt.style.use('ggplot')
plt.plot(x_values, y_values,
         color='steelblue',
         marker='o',
         markersize=3,
         )
plt.xlabel('迭代次数')
plt.ylabel('误差值')
plt.show()
