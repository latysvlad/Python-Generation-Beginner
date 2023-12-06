# Другая версия (концовка более сложная)

s = input()

if s.find("f") == -1:
    print(-2)
elif s.find("f") == s.rfind("f"):
    print(-1)
else:
    first_f = s.find("f")
    print(s[first_f + 1:].find("f") + first_f + 1)
