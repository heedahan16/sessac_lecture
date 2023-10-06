# 스팸 필터링을 NBC(나이브베이즈분류모델)을 쌩으로 구현해서 함수화하는 코드 작성

training_set = [["me free lottery", 1], ["free get free you", 1],  ["you free scholarship", 0], ["free to contact me", 0], ["you won award", 0], ["you ticket lottery", 1]]
test = ["free lottery"]

Normal_Set = {}
Spam_Set = {}

for sentence, label in training_set:
    if label == 0:
        for text in sentence.split(" "):
            if not text in Normal_Set:
                Normal_Set[text] = 0
            Normal_Set[text] += 1

    else:
        for text in sentence.split(" "):
            if not text in Normal_Set:
                Spam_Set[text] = 0
            Spam_Set[text] += 1

print("normal: ", Normal_Set)
print("spam: ", Spam_Set)

