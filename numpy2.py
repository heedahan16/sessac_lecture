# 1. 1에서 20사이의 균일한 간격으로 30개의 숫자를 만들고 2. 모든 값에 숫자 10을 더하는 코드 작성

import numpy as np

# 1에서 20사이의 균일한 간격으로 30개의 숫자를 만들기
print("step1")
num = np.linspace(1, 20, 30)
print(num)
print()

# 모든 값에 숫자 10을 더하기
print("step2")
print(num + 10)
print()