# 2) 질문: 주민등록번호 "901212-1234567"에서 생년월일을 추출하세요. 
#     (형식: "1990년 12월 12일")
#     파일명: id_number_parser.py
#     실행: python id_number_parser.py
#     결과: 1990년 12월 12일

num = "901212-1234567"
num_split = num.split("-")
birth = num_split[0]
year = "19" + birth[:2]
month = birth[2 : 4]
day = birth[4:]

print(f'{year}년 {month}월 {day}일')