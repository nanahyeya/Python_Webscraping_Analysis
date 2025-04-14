# 3) 질문: 입력된 이메일 주소가 유효한지 검사하세요. (조건: @와 . 포함)
#     (형식: "1990년 12월 12일")
#     파일명: email_validator.py
#     실행: python email_validator.py
#     결과: 이메일 주소: user@example.com
#     유효함
#     이메일 주소: user@example
#     유효하지 않음

email = input("your email: ")

if "@" in email and "." in email:
    print(f'이메일 주소: {email}')
    print("유효함")
else:
    print(f'이메일 주소: {email}')
    print("유효하지 않음")
