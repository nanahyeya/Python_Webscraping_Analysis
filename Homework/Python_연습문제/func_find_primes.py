# 3)  시작값, 끝값을 인자로 받아 그 사이의 소수를 리스트로 반환하는 find_primes 함수를 작성하세요. 
#     파일명: func_find_primes.py
#     find_primes() 함수를 선언
#     def find_primes(sentence):
#     실행: python func_find_primes.py

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    lis = []
    for num in range(start + 1, end):
        if is_prime(num):
            lis.append(num)
    return lis

start = int(input("시작값을 입력하세요: "))
end = int(input("끝값을 입력하세요: "))
print(find_primes(start, end))