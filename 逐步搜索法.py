import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
xl = -3
xr = 3
n = 1000


def f(x):
    f = x ** 3 - x - 1  # 需要求根的函数
    return f

xm_list = []
x_values = []
y_values = []
sum = 0
while True:
    h = (xr - xl) / n
    value = xl + h
    xm_list.append(value)
    sum += 1
    if f(value) == 0:
        break
    else:
        pass
    if f(value) < 0:
        xl=value
        value += h
    elif f(value) > 0:
        xr=value
        break

    if len(xm_list) > 1:
        error = abs((xm_list[-1] - xm_list[-2]) / xm_list[-1])
        x_values.append(sum)
        y_values.append(error)
        if error == 0:
            break
    else:
        pass
print(f'xl={xl},xr={xr}')
print(f'迭代第{sum}次后，误差为0,得到方程的根为：{value}')

plt.style.use('ggplot')
plt.plot(x_values, y_values,
         color='steelblue',
         marker='o',
         markersize=3,
         )
plt.xlabel('迭代次数')
plt.ylabel('误差值')
plt.show()
