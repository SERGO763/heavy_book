import functools
import operator
print(functools.reduce(lambda a,b: a*b, range(1, 6)))

n = 0
for i in range(1, 6):
    n ^= i
print(n)

print(functools.reduce(operator.xor, range(1, 6)))