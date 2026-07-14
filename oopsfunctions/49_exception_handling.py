# 49. Exception Handling Example
try:
    num = int("abc")
except ValueError:
    print("Invalid input: not a number")
finally:
    print("Execution finished")
