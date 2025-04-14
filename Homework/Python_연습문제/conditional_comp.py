# 7)  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 짝수는 제곱, 홀수는 그대로인 새 리스트를 생성하세요. (조건부 리스트 컴프리헨션 사용)
#     파일명: conditional_comp.py
#     실행: python conditional_comp.py
#     결과: 
#     [1, 4, 3, 16, 5, 36, 7, 64, 9, 100]

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [i ** 2 if (i % 2) == 0 else i for i in lis ]
print(new_list)
