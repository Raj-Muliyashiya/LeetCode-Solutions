nums = [1,12,-5,-6,50,3]
k = 4

maxx = 0

current_sum = sum(nums[0:k])
for i in range(k,len(nums)):
    current_sum = current_sum-nums[i-k]+nums[i]
    avg = current_sum/k
    maxx = max(maxx,avg)

print(maxx)


               