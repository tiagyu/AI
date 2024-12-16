# 문자열처리함수
python = 'Python is Amazing'
print(python.lower()) # 소문자로 변환
print(python.upper()) # 대문자로 변환
print(python[0].isupper()) # 대문자인지 확인
print(len(python)) # 글자수 확인
print(python.replace('Python','Java')) # 바꿔주는 함수, python을 java로 변환

index = python.index('n')
print(index)
index = python.index('n', index+1) # index+1 은 시작 위치를 업데이트 해줌 -> 첫 index 후에 n이 어디있는지 확인
print(index)

print(python.find('Java')) # 값이 없으면 -1을 출력
# print(python.index('Java')) # 값이 없으면 error가 나옴옴

print(python.count('n')) # n이 몇 번 등장하는지 확인

"""
이번 강의에서는 배운 함수들이 그래도 많았음 : 
lower
upper
isupper / islower
len
replace
index
find
count

"""