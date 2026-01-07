s = "ratt"
t = "car"


dic = {}

for i in range(len(s)):
    if not dic:
        if s[i] in dic:
            dic[s[i]] +=1
        else:
            dic[s[i]] = 1


print(dic)
        
