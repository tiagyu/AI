from sympy import Symbol, solve
k = Symbol('k')
equation = 8 - k / 2
answer = solve(equation)

print(answer)