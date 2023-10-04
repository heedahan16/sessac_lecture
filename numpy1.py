# x = [1, 2, 3, 4, 5, 6, 7, 8, 9], y=[10, 20, 30, 40, 50, 60, 70, 80, 90] 의 배열로 1. Numpy를 사용하여 3*3 행렬을 만든 뒤 2. 행렬합과 행렬곱을 구하는 코드 작성.

import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y=[10, 20, 30, 40, 50, 60, 70, 80, 90]

# Numpy를 사용하여 3*3 행렬 만들기
print("step1: x, y")
x = np.array(x).reshape(3, 3)
y = np.array(y).reshape(3, 3)
print( x)
print( y)
print()

# 행렬합
print("step2: x+y")
print( x+y)
print()

# 행렬곱
print("step3: x*y")
print(x.dot(y))
print()
