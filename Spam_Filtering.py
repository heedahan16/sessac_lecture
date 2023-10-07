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
      if not text in normal_frequncy:
        normal_frequncy[text] = 0
      normal_frequncy[text] += 1
  else:
    for text in sentence.split(" "):
      if not text in spam_frequncy:
        spam_frequncy[text] = 0
      spam_frequncy[text] += 1  

print("normal_frequncy: ", normal_frequncy)      
print("spam_frequncy: ", spam_frequncy)    
