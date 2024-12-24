# 지역변수와 전역변수
"""
지역 변수는 함수 내에서만 사용 가능
함수가 호출 될 때 만들어졌다가 함수 호출이 끝나면 사라지는 것

전역 변수는 모든 공간에서 부를 수 있음
프로그램 내에서 어디서든지 부를 수 있음
"""

gun = 10

def checkpoint(soldiers):# 경계근무
    gun = 20
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')
    
print(f'전체 총 : {gun}')
checkpoint(2) # 2명이 경계 근무 나감
print(f'남은 총 : {gun}')

"""
위 함수에서 gun=20을 지정해주지 않으면면 error가 난다
왜냐하면 함수 밖에서 gun은 지정 되었지만 함수 내에서 gun이 지정되지 않았기 때문
"""

gun = 10

def checkpoint(soldiers):# 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')
    
print(f'전체 총 : {gun}')
checkpoint(2) # 2명이 경계 근무 나감
print(f'남은 총 : {gun}')

def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers
    print(f'[함수 내] 남은 총 : {gun}')
    return gun

print(f'전체 총 : {gun}')
gun = checkpoint_ret(gun, 2)
print(f'남은 총 : {gun}')