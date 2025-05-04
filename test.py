import numpy as np
import matplotlib.pyplot as plt

# parameters
h = 0.001
k_max = 100

# initial z_k(0)=[x1,x2]^T
x1 = [1.0]  # x(0) = 1
x2 = [0.0]  # x'(0) = 0

# Euler method
for k in range(k_max):
    x1_new = x1[k] + h * x2[k]
    x2_new = x2[k] + h * (-3 * x2[k] - x1[k])
    x1.append(x1_new)
    x2.append(x2_new)

# k=1,2,3...100
k_list = list(range(k_max + 1))

# graph
plt.figure(figsize=(10,6))
plt.plot(k_list, x1, label="x_k", color='blue')
plt.plot(k_list, x2, label="x\'_k", color='red')
plt.xlabel("k")
plt.ylabel("x\'\' and x\'")
plt.title("solution of x\'\'+3x\'+x=0")
plt.legend()
plt.grid(True)
plt.show()
