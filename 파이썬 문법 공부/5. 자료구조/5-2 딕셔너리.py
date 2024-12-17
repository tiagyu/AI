# 딕셔너리
cabinet = {3 : '유재석', 100 : '김태호'}
print(cabinet[3])
print(cabinet[100]) # []을 이용해서 값을 불러올 경우 없는 값이면 에러가 뜸

print(cabinet.get(3)) # get 함수를 이용해서 값을 불러올 경우 없는 값이면 None이라고 뜨고 다음 코드 실행
print(cabinet.get(5))
print(cabinet.get(10, '새로운 값 넣기'))

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {'A-3' : '유재석', 'B-100' : '김태호'}
print(cabinet['A-3'])
print(cabinet['B-100'])

# 새 손님
print(cabinet)
cabinet['A-3'] = '김종국'
cabinet['C-20'] = '조세호'
print(cabinet)

# 간 손님 : 키 삭제
del cabinet['A-3']
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐쩜
cabinet.clear()
print(cabinet)