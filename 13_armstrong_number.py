# 13. Armstrong Number Check
n = 153
digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)
print(total == n)
