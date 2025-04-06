from sympy import Symbol, solve
k = Symbol('k')
equation = 2*k-10
answer = solve(equation)

print(answer)