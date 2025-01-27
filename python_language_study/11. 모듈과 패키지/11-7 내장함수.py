# 내장함수
"""
import 할 필요 없이 사용 가능한 함수

예:
import : 사용자 입력을 받는 함수
dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

구글 built in function python -- 내장 함수 볼 수 있음

"""

sports = input('무슨 운동을 좋아하나요?')
print(f'{sports}를 좋아합니다')

# dir
# 아무것도 넣지 않은 경우
print(dir()) # 현재 스코프에서 사용 가능한 이름 리스트를 보여줌

# 특정 객체의 속성 확인
my_list = [1,2,3,4]
print(dir(my_list)) # 리스트 객체가 가진 모든 매서드와 속성을 반환 예를 들어 append, pop 등을 보여줌

letter = 'name'
print(dir(letter))

# 특정 모듈 탐색
import random # 외장함수
print(dir(random)) # random 함수 내에서 쓸 수 있는 함수 표시
