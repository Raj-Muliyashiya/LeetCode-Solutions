# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [100,4,200,1,3,2]
nums = [1,2,6,7,8]


hashset = set(nums)
max_streak = 0

for num in hashset:
    if (num-1) not in hashset:
        current = num
        current_streak = 1

        while (current + 1) in hashset:
            current +=1
            current_streak +=1

        max_streak = max(max_streak,current_streak) 


print(max_streak)
