"""
quiz) 당신은 cocoa 서비스를 이용하는 택시 기사다
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성해라

조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해진다
조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 한다

(출력문 예제)
[0] 1번째 손님 (소요시간 :15분)
[ ] 2번째 손님 (소요시간 :50분)
[0] 3번째 손님 (소요시간 :5분)
.....

[ ] 50번째 손님 (소요시간 :16분)

총 탑승 승객 : 2분
"""

# 내 풀이
from random import *

def taxi():
    passenger = []
    total = 0
    for i in range(1,51):
        time = randrange(5,50)
        passenger.append([i,time])
        if 5 <= passenger[i-1][1] <=15:
            total+=1
            print(f'[0] {i}번째 손님 (소요시간 : {time}분)')
        else:
            print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')
    print()
    print(f'총 탑승 승객 : {total}분')

taxi()

# 다른 사람 풀이
from random import *
count = 0 # 총 탑승 승객 수
for i in range(1,51): # 1에서 50이라는 수
    time = randrange(5,51) # 5분~50분 소요 시간
    if 5<= time <= 15: # 5분~15분 이내의 손님 탑승 수 증가 처리(매칭 성공)
        print(f'[0] {i}번째 손님 (소요시간 : {time}분)')
        count += 1
    else: # 매칭 실패한 경우
        print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')

print(f'총 탑승 승객 : {count}분')