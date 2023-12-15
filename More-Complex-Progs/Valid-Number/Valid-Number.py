a = input().split("-")
ls = [len(i) for i in a]

if ls == [1, 3, 3, 4] and "".join(a).isdigit() and a[0] == "7":
    print("YES")
elif ls == [3, 3, 4] and "".join(a).isdigit():
    print("YES")
else:
    print("NO")
