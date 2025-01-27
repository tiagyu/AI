"""
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

 * 표준 체중 : 각 개인의 키에 적당한 체중
 
 (성별에 따른 공식)
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21
 
 조건1: 표준 체중은 별도의 함수 내에서 계산
        - 함수명 : std_weight
        - 전달값 : 키(height), 성별(gender)
 조건2 : 표준 체중은 소수점 둘째자리까지 표시
 
 (출력예제)
 키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""

# 내 풀이
def std_weight(height,gender):
    if gender == '남자':
        weight = (height * height * 22) / 10000
        weight = round(weight,2)
    else:
        weight = (height * height * 21) / 10000
        weight = round(weight,2)
        
    return f'키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.'

print(std_weight(height=175, gender='남자'))

# 다른 사람 풀이
def std_weight(height, gender): # 키 m 단위(실수), 성별 '남자' /'여자'
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21
    
height = 175 # cm 단위
gender = '남자'
weight = round(std_weight(height / 100, gender), 2)
print(f'키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.')