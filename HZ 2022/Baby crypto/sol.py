from sympy.ntheory import discrete_log

p = 333870410550569
g = 3
A = 146771267179515

a = discrete_log(p, A, g)
print('HZ{' + str(a) + '}')

# OUTPUT : HZ{39763325028139}