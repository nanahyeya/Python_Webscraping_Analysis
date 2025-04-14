# 2)  문자열을 인자로 받아 단어 수를 반환하는 count_words 함수를 작성하세요.   
#      파일명: func_count_words.py
#      count_words() 함수를 선언
#      def count_words(sentence):
#      실행: python func_count_words.py
#      결과: 단어 수: 5

def count_words(sentence):
    
    return len(sentence)

sentence = input('문장을 입력해 주세요: ')

print(f'단어 수수: {count_words(sentence)}')