# 23. Count Vowels in a String
s = "Hello World"
count = sum(1 for ch in s.lower() if ch in "aeiou")
print("Vowels:", count)
