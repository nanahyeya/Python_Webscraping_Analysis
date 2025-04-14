# 2)  [10, 20, 30, 40, 50]에서 30보다 큰 수만 필터링하세요. 
#     (filter 함수 사용)   
#     파일명: filter_func.py
#     실행: python filter_func.py
#     결과: [40, 50]

lis = [10, 20, 30, 40, 50]
lis2 = [i for i in lis if i > 30]

print(lis2)