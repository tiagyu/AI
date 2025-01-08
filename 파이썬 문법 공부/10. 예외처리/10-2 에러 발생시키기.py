# 에러 발생시키기
"""
raise 함수를 이용해서 error를 만들고 이용
"""
try:
    print('축의금 계산기')
    number1 = int(input('첫 번쨰 결혼 순서 : '))
    number2 = int(input('두 번쨰 결혼 순서 : '))
    if number1 >= 5 or number2 >= 5:
        raise ValueError
    print(f'{number1} / {number2} = {int(number1 + number2)}')
except ValueError:
    print('잘못된 값을 입력하였다. 하나만 입력하세요')