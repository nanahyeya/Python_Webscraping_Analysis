# 3) 질문: 12345초를 시간, 분, 초로 변환하세요. 
#      (공식: 시 = 총초 //3600, 나머지초 = 총초 % 3600, 
#          분 = 나머지초 // 60,  초 = 나머지초 % 60)
#     파일명: time_converter.py
#     실행: python time_converter.py
#     결과: 12345초는 3시간 25분 45초입니다.

sec = 12345
hour = 12345 // 3600
minute = (sec - (hour * 3600)) // 60
second = (sec - (hour * 3600)) - (minute * 60)

print(f'{sec}초는 {hour}시간 {minute}분 {second}초 입니다.')