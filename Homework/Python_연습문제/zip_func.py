# 3)  두 리스트 [1, 2, 3]과 [10, 20, 30]의 요소들을 짝지어 출력하세요. 
#     (zip 함수 사용)
#     파일명: zip_func.py
#     실행: python zip_func.py
#     결과: 
#     1 10
#     2 20
#     3 30

lis1 = [1, 2, 3]
lis2 = [10, 20, 30]
for a,  b in zip(lis1, lis2):
    print(a, b)