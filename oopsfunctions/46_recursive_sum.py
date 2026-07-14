# 46. Recursion - Sum of N Natural Numbers
def recursive_sum(n):
    return n if n <= 1 else n + recursive_sum(n - 1)

print(recursive_sum(10))
