# 4)  질문: 10000원을 3명이서 똑같이 나누어 가질 때 각자 얼마를 받고 얼마가 남는지 계산하세요.
#      파일명: money_divide.py
#    실행: python money_divide.py
#    결과: 각자 3333원을 받고 1원이 남습니다

money = 10000
people = 3
pay = 10000 // 3
rest = money - (pay * 3)

print(f'각자 {pay}원을 받고 {rest}원이 남습니다')