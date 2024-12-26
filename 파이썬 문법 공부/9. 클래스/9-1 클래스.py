# 클래스
"""
class는 붕어빵 기계에 비유를 한다
붕어빵 기계는 붕어빵 틀이 있으며 틀에다가 재료를 넣으면 
틀에 맞춰서 붕어빵이 나온다 -> 틀은 하나이지만 붕어빵은 무한
"""

# 마린 : 공격 유닛, 군인, 총을 쓸 수 잇음
name = '마린' # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print(f'{name} 유닛이 생성되었습니다')
print(f'체력 {hp}, 공격력 {damage}\n')

# 탱크 : 공격 유닛, 탱크. 포를 쓸 수 있는데, 일반 모드 / 시즈 모드
tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print(f'{tank_name} 유닛이 생성되었습니다')
print(f'체력 {tank_hp}, 공격력 {tank_damage}\n')

tank2_name = '탱크'
tank2_hp = 150
tank2_damage = 35

print(f'{tank2_name} 유닛이 생성되었습니다')
print(f'체력 {tank2_hp}, 공격력 {tank2_damage}\n')


def attack(name, location, damage):
    print(f'{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]')

attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)
attack(tank_name, '1시', tank2_damage)

# 위 코드를 클래스로 변환
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다')
        print(f'체력 {self.hp}, 공격력 {self.damage}')
        
marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)