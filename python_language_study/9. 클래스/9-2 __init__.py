# __init__
"""
class로 만들어지는 녀석들을 객체라고 한다
여기서 마린과 탱크는 unit 클래스의 인스턴스라고 한다
self 변수명을 제외하고서 나머지 변수들이 지정되어야지만 실행 가능함
"""

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