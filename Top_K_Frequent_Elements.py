nums = [4,1,-1,2,-1,2,3]
k = 2

dic = {}

for i in nums:
    dic[i] = 1 + dic.get(i,0)


sort = sorted(dic.items(),key=lambda x: x[1],reverse=True)

print(sort)