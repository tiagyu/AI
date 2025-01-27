# 문자열 포맷
print('a' + 'b')
print('a','b')

# 방법 1
print('나는 %d살입니다.' % 20) # d는 정수값이기 때문에 정수값만 넣을 수 있음
print('나는 %s을 좋아해요' %'파이썬') # s는 문자열 값이다
print('Apple은 %c로 시작해요' %'A') # c는 문자 값이다
# s% 를 시작하면 모두 사용가능하다

print('나는 %s색과 %s색을 좋아해요.' %('파란','빨간'))

# 방법 2
print('나는 {}살입니다'.format(20))
print('나는 {}색과 {}색을 좋아해요.' .format('파란','빨간'))
print('나는 {1}색과 {0}색을 좋아해요.' .format('파란','빨간'))

# 방법 3
print('나는 {age}살이며, {color}색을 좋아해요' .format(age = 20, color = '빨강'))
print('나는 {age}살이며, {color}색을 좋아해요' .format(color = '빨강', age = 20))

# 방법 4
age = 20
color = 'orange'
print(f'나는 {age}살이며, {color}색을 좋아해요')