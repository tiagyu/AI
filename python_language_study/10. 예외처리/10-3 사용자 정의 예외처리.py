# 사용자 정의 예외처리
"""
사용자가 원하는 class로 에러를 만든 다음에 디버깅할 수 있음음
"""
class BigNumberError(Exception):
    def __init__(self, letter):
        self.letter = letter
        
    def __str__(self):
        return self.letter

try:
    print('축의금 계산기')
    number1 = int(input('첫 번쨰 결혼 순서 : '))
    number2 = int(input('두 번쨰 결혼 순서 : '))
    if number1 >= 5 or number2 >= 5:
        raise BigNumberError(f'입력값 : {number1}, {number2}')
    print(f'{number1} / {number2} = {int(number1 + number2)}')
except ValueError:
    print('잘못된 값을 입력하였다. 하나만 입력하세요')
except BigNumberError as err:
    print('숫자가 너무 큽니다')
    print(err)