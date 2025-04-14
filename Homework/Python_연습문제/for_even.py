# 1) 질문: 1부터 10까지의 숫자 중 짝수만 출력하세요.
#     파일명: for_even.py
#     실행: python for_even.py
#     결과: 
#     2
#     4
#     6
#     8
#     10

for i in range(1, 11):
    if (i % 2) == 0:
        print(i)