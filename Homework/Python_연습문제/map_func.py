# 6)   두 리스트 [1, 2, 3]과 [4, 5, 6]의 각 요소를 더한 새 리스트를 생성하세요. (map 함수 사용)
#      파일명: map_func.py
#      실행: python map_func.py
#      결과: 
#      [5, 7, 9]

lis = [1, 2, 3]
lis2 = [4, 5, 6]
new_lis = list(map(lambda x, y: x + y, lis, lis2))

print(new_lis)