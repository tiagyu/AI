# finally
"""
예외처리 구문에서 정상 or 오류나도
finally 구문은 무조건 실행되는 구문
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
finally:
    print('finally는 무조건 작동됨')