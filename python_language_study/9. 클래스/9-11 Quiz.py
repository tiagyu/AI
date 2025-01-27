"""
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

(출력 예제)
총 3대의 매물이 있습니다
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
"""

# 코드
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, complete_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.complete_year = complete_year
    
# 매물 정보 표시
    def detail(self):
        print(f'{self.location} {self.house_type} {self.deal_type} {self.price} {self.complete_year}')

# House 인스턴스 생성
houses = [
    House("강남", "아파트", "매매", "10억", "2010년"),
    House("마포", "오피스텔", "전세", "5억", "2007년"),
    House("송파", "빌라", "월세", "500/50", "2000년"),
]

# 매물 정보 출력
print(f"총 {len(houses)}대의 매물이 있습니다.")
for house in houses:
    house.detail()
    
## 강의 코드
class House1:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, complete_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.complete_year = complete_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.complete_year)

house = []
house1 = House1('강남','아파트','매매','10억','2010년')
house2 = House1("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House1("송파", "빌라", "월세", "500/50", "2000년")
house.append(house1)
house.append(house2)
house.append(house3)

print(f'총 {len(house)}대의 매물이 있습니다.')
for home in house:
    home.show_detail()