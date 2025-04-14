# 4) 질문: "Python is awesome"에서 모음(a, e, i, o, u)의 개수를 세세요.
#      파일명: count_vowels.py
#     실행: python count_vowels.py
#     결과: 모음 개수 : 6

sentence = "Python is awesome"

count = 0
for w in sentence:
    if w in "aeiouAEIOU":
        count += 1

print(count)