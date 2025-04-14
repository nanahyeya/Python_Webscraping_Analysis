# 1)  두 수와 연산자(+, -, *, /)를 인자로 받아 계산하는 calculator 함수를 작성하세요.    
# 파일명: func_calculator.py

# calculator() 함수를 선언
# def calculator(a, b, op):

# 실행: python func_calculator.py
# 결과: [1, 4, 9, 16, 25]

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "0으로 나눌 수 없습니다."
    else:
        return "지원하지 않는 연산자입니다."
    

a = float(input("첫 번째 숫자를 입력하세요: "))
b = float(input("두 번째 숫자를 입력하세요: "))
op = input("연산자를 입력하세요: ")

print(calculator(a, b, op))