# 2) 질문: {"name": "John", "age": 30} 딕셔너리에서 "age"의 값을 출력하세요.
#     {"math": 90, "science": 85, "history": 78} 딕셔너리에서 모든 과목명을 출력하세요.
#     딕셔너리 {'apple': 3, 'banana': 5}에서 apple의 값을 2 증가시키세요.
#     [5, 2, 8, 1, 9] 리스트를 오름차순으로 정렬하세요.
#     파일명: dict_process.py
#     실행: python dict_process.py
#     결과:  나이: 30
#     과목들: ['math', 'science', 'history'] 
#     {'apple': 5, 'banana': 5}

dic = {"name": "John", "age": 30}
dic2 = {"math": 90, "science": 85, "history": 78}
list2 = []
for sub in dic2.keys():
    list2.append(sub)
dic3 = {'apple': 3, 'banana': 5}
dic3['apple'] += 2

print(f'나이: {dic["age"]}')
print(f'과목들: {list2}')
print(dic3)
