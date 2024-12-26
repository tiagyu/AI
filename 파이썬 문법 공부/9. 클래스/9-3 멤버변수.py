# 멤버변수
"""
멤버변수란 class내에서 정의된 변수라고 한다

파이썬은 class 외부에서 내가 원하는 변수에 대해서 확장을 할 수도 있고 
그 확장된 변수는 확장을 한 객체에 대해서만 적용이 된다
"""

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다')
        print(f'체력 {self.hp}, 공격력 {self.damage}')
        
# marine1 = Unit('마린', 40, 5)
# marine2 = Unit('마린', 40, 5)
# tank = Unit('탱크', 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit('레이스','80',5)
print(f'유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}')

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit('뺴앗은 레이스','80',5)
wraith2.clocking = True

if wraith2.clocking == True:
    print(f'{wraith2.name}는 현재 클로킹 상태입니다.')