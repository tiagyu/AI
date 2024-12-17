# 튜플
# 변경은 되지 않지만 리스트 보다 튜플이 속도가 빠름

menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])

# menu.add('생선까스') -> 오류

name = '김종국'
age = 20
hobby = '코딩'
print(name, age, hobby)

(name, age, hobby) = ('김종국', 20, '코딩')
print((name, age, hobby))