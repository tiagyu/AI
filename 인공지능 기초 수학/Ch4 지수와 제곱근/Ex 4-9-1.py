# 파이썬 Sympy의 expand, factor, Symbol을 호출하고 기호변수 x를 선언한다
from sympy import expand, factor, Symbol
x = Symbol('x')

# expand()는 수식을 (x+1) * (x+5)로 전개한다
exp = expand((x+1)*(x+5))
print(exp)

# factor()는 인수분해하는 함수로, x2+6x+5를 인수분해한다
fac = factor(x**2 + 6*x + 5)
print(fac)

# 연습문제1
x = Symbol('x')
y = Symbol('y')
problem1 = factor(x**3*y - x*y**3)
print(problem1)

# 연습문제2
x = Symbol('x')
y = Symbol('y')
problem2 = factor(x**2+3*x+2)
print(problem2)