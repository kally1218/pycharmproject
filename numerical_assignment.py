import numpy as np
import matplotlib.pyplot as plt

def euler_method(t_end, h):
    # 初始化值
    y1 = 1  # x(0) = 1
    y2 = 0  # x'(0) = 0

    # 时间长度
    t = np.arange(0, t_end, h)
    y1_values = [y1]
    y2_values = [y2]

    # 欧拉法迭代
    for _ in t[1:]:
        y1_new = y1 + h * y2
        y2_new = y2 + h * (-3 * y2 - y1)
        y1_values.append(y1_new)
        y2_values.append(y2_new)
        y1, y2 = y1_new, y2_new

    return t, y1_values, y2_values

t_end = 100
h = 0.001

t, x_values, dx_values = euler_method(t_end, h)

plt.figure(figsize=(10, 6))
plt.plot(t, x_values, label='x(t)', color='blue')  # 绘制 x(t)
plt.plot(t, dx_values, label="x'(t)", color='red')  # 绘制 x'(t)

plt.xlabel('t')
plt.ylabel('Values')
plt.title('Solution of ẍ + 3ẋ + x = 0 using Euler Method')
plt.legend()
plt.grid(True)
plt.savefig("./result.png")
plt.show()