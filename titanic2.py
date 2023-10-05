# titanic_train.csv  파일을 불러와서 1. 30대이면서 1등석에 탄 사람의 수 2. 클래스(Pclass)별 나이 평균 3. 클래스(Pclass)와 성별에 따른 생존율 4. 나이(Age)대 별로 생존율 구하기

import pandas as pd
import numpy as np

# titanic_train.csv  파일을 불러오기
titanic = pd.read_csv("titanic_train.csv")
print(titanic)

titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

def Age_Range(n):
    if n < 10:
       return 0
    elif n >= 10 and n < 20:
        return 10
    elif n >= 20 and n < 30:
        return 20
    elif n >= 30 and n < 40:
        return 30
    elif n >= 40 and n < 50:
        return 40
    elif n >= 50 and n < 60:
        return 50
    elif n >= 60 and n < 70:
        return 60
    elif n >=  70 and n < 80:
        return  70
    else:
        return 80

titanic["Age_Range"] = titanic["Age"].apply(Age_Range)
print(titanic["Age_Range"])
print()

# 30대이면서 1등석에 탄 사람의 수 
print("step1")
print(np.where((titanic["Age_Range"] == "30대") & (titanic["Pclass"] == 1), 1, 0).sum())
print()

# 클래스(Pclass)별 나이 평균 
print("step2")
print(titanic.groupby("Pclass")["Age"].mean())
print()

# 클래스(Pclass)와 성별에 따른 생존율 
print("step3")
pclassSex_survived_rate = titanic.groupby(["Pclass", "Sex"])["Survived"].sum()/titanic.groupby(["Pclass", "Sex"])["Survived"].count()
print(pclassSex_survived_rate)
print()

# 나이(Age)대 별로 생존율 구하기
print("step4")
age_survived_rate = titanic.groupby("Age_Range")["Survived"].sum()/titanic.groupby("Age_Range")["Survived"].count()
print(age_survived_rate.reindex([0, 10, 20, 30, 40, 50, 60, 70, 80]))
print()