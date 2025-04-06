#SymPy 라이브러리를 불러오고 사용할 기호 변수 k를 선언한다
from sympy import solve, Symbol
x = Symbol('x')
y = Symbol('y')

# 방정식을 풀려면 '일차방정식 = 0'으로 만들어 주어야 한다
# 이를 위해 모든 식을 좌변으로 이항한 후 equation1과 equation2로 변수화한다
equation1 = 3 * x + y - 2
equation2 = x - 2 * y - 3

# 방정식을 풀려면 Sympy에 내장된 solve()함수를 사용
answer = solve((equation1,equation2), dict=True) #dict 옵션은 해를 딕셔너리 형태로 변환한다

print(answer)