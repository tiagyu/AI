# while
customer = '토르'
index = 5
while index >=1 :
    print(f'{customer}, 커피가 준비 되었습니다 {index} 번 남았어요')
    index -= 1
    if index == 0:
        print('커피는 폐기처분되었습니다')
    
# 무한루프    
# customer2 = '아이언맨'
# index = 1
# while True:
#     print(f'{customer2}, 커피가 준비 되었습니다 호출 {index}번')
#     index += 1

customer3 = '토르'
person = 'unknown'

while person != customer3 :
    print(f'{customer3} 커피가 준비 되었습니다')
    person = input('이름이 어떻게 되세요? ')
