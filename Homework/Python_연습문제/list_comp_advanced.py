# 4)  [1, 2, 3, 4, 5]의 각 요소에 10을 더한 후 2로 나눈 결과를 리스트로 생성하세요. (리스트 컴프리헨션 사용)
#     파일명: list_comp_advanced.py
#     실행: python list_comp_advanced.py
#     결과: 
#     [5.5, 6.0, 6.5, 7.0, 7.5]

lis = [1, 2, 3, 4, 5]
lis = [(i + 10) / 2 for i in lis]

print(lis)