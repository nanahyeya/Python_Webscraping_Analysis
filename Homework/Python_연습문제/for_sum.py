# 2) 질문: 1부터 100까지의 숫자 중 3의 배수의 합을 구하세요.
#     파일명: for_sum.py
#     실행: python for_sum.py
#     결과: 3의 배수의 합: 1683

s = 0
for num in range(1,101):
    if (num % 3) == 0:
        s += num
        

print(f'3의 배수의 합: {s}')