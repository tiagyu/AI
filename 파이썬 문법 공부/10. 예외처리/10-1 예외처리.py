# 예외처리
try:
    print('곱하기 전용 계산기')
    number1 = int(input('첫 번째 숫자를 입력하세요'))
    number2 = int(input('두 번째 숫자를 입력하세요'))
    print(f'{number1} / {number2} = int({number1/number2})')
except ValueError:
    print('에러! 잘못된 값을 입력하였습니다')
except ZeroDivisionError as err:
    print(err)
    
# 예외처리2
try:
    print('음료수 자판기')
    box = []
    box.append(input('첫 번째 음료수'))
    box.append(input('두 번째 음료수'))
    # box.append(box[0]+box[1])1
    print(f'음료수 종료는 {box[0]}, {box[1]}이 있고 둘을 섞으면 {box[2]}')
except Exception as err:
    print(err)