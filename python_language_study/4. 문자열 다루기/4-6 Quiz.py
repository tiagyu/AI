"""
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예 ) http://naver.com

규칙 1 : http:// 부분은 제외 -> naver.com
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성

출력 예시 : nav51!
"""

address = 'http://naver.com'

def password(site):
    let = site.replace('http://','')
    letter = let.replace('.com','')
    
    r1 = letter[:3]
    r2 = len(letter)
    r3 = letter.count('e')
    r4 = '!'
    
    return f'{r1}{r2}{r3}{r4}'

print(password(address))

# 풀이 방법

url = 'http://naver.com'
my_str = url.replace('http://','') # 규칙 1
my_str = my_str[:my_str.index('.')] # my_str[0:5] -> 0~5 직전까지 : 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print('{0}의 비밀번호는 {1}입니다.' .format(url, password))
