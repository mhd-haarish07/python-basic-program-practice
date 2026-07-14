# 15. LCM of Two Numbers
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

print(lcm(4, 6))
