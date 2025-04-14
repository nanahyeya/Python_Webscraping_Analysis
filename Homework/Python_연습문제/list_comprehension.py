#  1)  리스트 [1, 2, 3, 4, 5]의 각 요소를 제곱한 새 리스트를 생성하세요.    
#      (List Comprehension 사용)
#      파일명: list_comprehension.py
#      실행: python list_comprehension.py
#      결과: [1, 4, 9, 16, 25]


lis = [1, 2, 3, 4, 5]
lis2 = [i ** 2 for i in lis]
print(lis2)
