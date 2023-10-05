# 스팸 필터링을 NBC(나이브베이즈분류모델)을 쌩으로 구현해서 함수화하는 코드 작성

training_set = [["me free lottery", 1], ["free get free you", 1],  ["you free sholarship", 0], ["free to contact me", 0], ["you won award", 0], ["you ticket lottery", 1]]
test = ["free lottery"]

Classfication = ["award", "contact", "free", "get", "lottery", "me", "scholarship", "ticket", "to", "won", "you"]

Normal_Text = []
Spam_Text = []
    
for training in training_set:
    for text in training[0].split(" "):
        if training[1] == 0:
            Normal_Text.append(text)
        else:
            Spam_Text.append(text)

print(Normal_Text)
print(Spam_Text)