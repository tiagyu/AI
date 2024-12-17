# 리스트 []

"""
이번 강의에서 배운 함수들 정리
index () : 몇 번째 위치에 있는지 알려주는 함수
append () : 리스트에 추가해주는 함수
insert () : 리스트에 추가를 하는데 원하는 위치에 추가를 할 수 있음
pop () : 리스트에서 맨 뒤에 값을 삭제해줌
count () : 내가 찾고자 하는 것이 몇 개 있는지 확인해줌
sort () : 정렬 함 (알파벳 순서, 숫자 순서)
reverse () : 거꾸로 정렬 함
clear () : 리스트 안에 있는 내용 모두 삭제
extend () : 리스트들을 합쳐주는 함수
"""

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ['유재석', '조세호', '박명수']
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index('조세호'))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append('하하')
print(subway)

# 정ㅇ형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, '정형돈')
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append('유재석')
print(subway)
print(subway.count('유재석'))

# 정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,4,3,2,1]
mx_list = ['조세호', 20, True]
print(mx_list)

# 리스트 확장
num_list.extend(mx_list)
print(num_list)
