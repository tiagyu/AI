# 세트 : 집합 (set)
# 중복 안됨, 순서 없음

"""
집합에 대해서 공부함
set 함수를 이용해서 중복 제거는 알고 있었는데 이렇게 사용하는거구나
그리고 {}를 이용해서도 만들 수 잇는 거를 처음 알게 됨

& | 는 알고 있었는데 - 로 차집합도 할 수 있구나
intersection () : and 함수
union () : 합집합
differnece () : 차집합

add와 remove는 이 set에서만 가능한건가..?? 아마 아닐것 같음
그러면 add와 append의 차이가 뭐지??
---------------------------------
add() 는 집합 자료형에서 사용되고 append()는 리스트 자료형에서 사용된다
remove 함수는 둘 다 사용가능하지만 차이가 있음
1) 리스트 : 중복된 값이 있으면 앞의 값 하나만 삭제
2) 집합 : 집합에서 특정 값을 삭제제

"""

my_set = {1,2,3,3,3}
print(my_set)

java = {'유재석', '김태호', '양세형'}
python = set(['유재석','박명수'])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차 집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add('김태호')
print(python)

# java를 까먹음
java.remove('김태호')
print(java)