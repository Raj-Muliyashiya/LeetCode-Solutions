s = "rat"
t = "car"


dic = {}

for i in range(len(s)):
    dic[i] = s[i]
    print(f"add{s[i]}")

    if len(dic) == len(t):
        print('a')
        print(t[i] in dic.values())

print('none')