import numpy as np

A = np.array([[1, 2], [2, 4.004]])
cond = np.linalg.cond(A)
print(cond)
