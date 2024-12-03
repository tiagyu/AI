#SymPy 라이브러리를 불러오고 사용할 기호 변수 k를 선언한다
from sympy import Symbol, solve
k = Symbol('k')
equation = k-2-4
answer = solve(equation)

print(answer)