# 모듈
"""
class, def를 담고있는 파일을 모듈이라고 한다
"""
# 일반 가격
def popcorn(price):
    print(f'5명 팝콘의 가격은 {int(price * 5)}원 입니다')
    
# 쿠폰 할인 가격
def coupon(price):
    print(f'5명 팝콘의 가격은 {int((price * 5) * 0.8)}원 입니다')
    
# 군인 할인 가격
def soldier(price):
    print(f'5명 팝콘의 가격은 {int((price * 5) * 0.4)}원 입니다')

