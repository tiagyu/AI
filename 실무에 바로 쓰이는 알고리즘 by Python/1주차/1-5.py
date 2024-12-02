# class 배우기
class Calculator:
    # 클래스 구현체를 인스턴스라고 한다
    # '시작'한다고 하여 init 메소드를 항상 호출한다
    # 앞뒤로 붙은 __ 기호는 매직 매소드(미리 예약된 메소드)들을 위한 기초이다.
    def __init__(self,number):
        self.number = number
    
    def plus(self,number2):
        print(self.number + number2)
        
pl = Calculator(5)
pl.plus(10)