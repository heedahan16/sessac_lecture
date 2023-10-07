# 스팸필터링을 NBC(나이브베이즈분류 모델)을 쌩으로 구현해서 함수화하기

training_set = [["me free lottery", 1], ["free get free you", 1],  ["you free scholarship", 0], ["free to contact me", 0], ["you won award", 0], ["you ticket lottery", 1]]
test = ["free lottery"]

# 전처리: 단어를 공백으로 분리하여, 단어별 빈도수 세기
print("step1: 전처리(단어를 공백으로 분리하여, 단어별 빈도수 세기)")
print()

normal_frequncy = {"award":0, "contact":0, "free":0, "get":0, "lottery":0, "me":0, "scholarship":0, "ticket":0, "to":0, "won":0, "you":0}
spam_frequncy = {"award":0, "contact":0, "free":0, "get":0, "lottery":0, "me":0, "scholarship":0, "ticket":0, "to":0, "won":0, "you":0}

for sentence, label in training_set:
    if label == 0:
        for text in sentence.split(" "):
            normal_frequncy[text] += 1
    else:
        for text in sentence.split(" "):
            spam_frequncy[text] += 1  

print("normal_frequncy: ", normal_frequncy)      
print("spam_frequncy: ", spam_frequncy)    

# 스팸/정상일 경우 조건부 확률 계산: 각 단어빈도를 활용하여 스팸/정상일 경우 조건부 확률 계산(라플라스 스무딩 적용)
print()
print("step2: 스팸/정상일 경우 조건부 확률 계산: 각 단어빈도를 활용하여 스팸/정상일 경우 조건부 확률 계산(라플라스 스무딩 적용))")
print()
normal_probability = {"award":0, "contact":0, "free":0, "get":0, "lottery":0, "me":0, "scholarship":0, "ticket":0, "to":0, "won":0, "you":0}
spam_probability = {"award":0, "contact":0, "free":0, "get":0, "lottery":0, "me":0, "scholarship":0, "ticket":0, "to":0, "won":0, "you":0}

total_normal = 0
total_spam = 0

for total in normal_frequncy.values():
    total_normal += total
for total in spam_frequncy.values():
    total_spam += total

k = 0.5

print("<normal_probability>")
for key, cnt_normal in normal_frequncy.items():
    normal_probability[key] = (k + cnt_normal )/ (2*k + total_normal)

    print(key, normal_probability[key])

print()
print("<spam_probability>")
for key, cnt_spam in spam_frequncy.items():
    spam_probability[key] = (k + cnt_spam) / (2*k + total_spam)

    print(key, spam_probability[key])

# 조건부 확률에 로그 적용
print()
print("step3: 조건부 확률에 로그 적용")
print()

import math

print("< log_normal_conditional_probability >")
for key, normal_conditional_probability in normal_probability.items():
    print(key, math.log(normal_conditional_probability))

print()
print("< log_spam_conditional_probability >")
for key, spam_conditional_probability in spam_probability.items():
    print(key, math.log(spam_conditional_probability))

