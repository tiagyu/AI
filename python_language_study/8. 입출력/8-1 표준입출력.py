# 표준입출력
"""
sep= : 결과값을 무엇으로 나눌지 정하는 것
end= : 결과값을 이어서 붙임
ljust(8) : 왼쪽으로 정렬을 하는데 8공간 확보를 한 상태후에
zfill(3) : 0으로 나머지를 채우는데 3공간 내에서 001, 002 등
"""

print('Python', 'Java', sep=',', end='?')
print('무엇이 더 재밌을까요?')

import sys
print('Python', 'Java', file=sys.stdout) # 표준 출력으로 출력
print('Python', 'Java', file=sys.stderr) # 표준 에러로 출력

# 시험성적
scores = {'수학':0, '영어':50, '코딩':100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=':')
    
# 은행 대기순번표
# 001, 002, 003
for num in range(1,21):
    print('대기번호 : ' + str(num).zfill(3))
    
# 표준 입력
answer = input('아무 값이나 입력하세요 : ')
print('입력하신 값은 '+ answer + '입니다.')