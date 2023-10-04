# x=[np.nan, 1, 2, 3, 4, 5], y=pd.Series([x[np.random.randint(0, 6)] for i in range(20)]) 코드를 실행하고 Series Y에서 1. 결측값의 개수를 구하고 2. 결측값을 제거한 Series를 만들고 3. 결측값에 y의 평균값을 넣은 Series를 만드는 코드 작성

import pandas as pd
import numpy as np

# 코드 실행
x=[np.nan, 1, 2, 3, 4, 5]
y=pd.Series([x[np.random.randint(0, 6)] for i in range(20)]) 
print(x)
print(y)
print()

# 결측값의 개수를 구하고 
print("step1")
print(y.isnull().sum())
print()

# 결측값을 제거한 Series를 만들고 
print("step2")
print(y.dropna())
print()

# 결측값에 y의 평균값을 넣은 Series를 만드는 코드 작성
print("step3")
print(y.fillna(y.mean()))
print()