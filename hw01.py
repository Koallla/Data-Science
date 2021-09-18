import itertools 
import numpy as np

# 3
a_m = np.array([[3, 0, 3], [6, 1, 0], [1, 1, 1]])
b_m = np.array([1, 1, 1])

u, v, w = np.linalg.solve(a_m, b_m)

a = (1/np.sqrt(u), -1/np.sqrt(u))
b = (1/np.sqrt(v), -1/np.sqrt(v))
c = (1/np.sqrt(w), -1/np.sqrt(w))

res = list(itertools.product(a, b, c))



# 4
a_m = np.array([[1, 1, 1], [9, 3, 1], [-1, -1, 1]])
b_m = np.array([[12], [54], [2]])

a, b, c = np.linalg.solve(a_m, b_m)


