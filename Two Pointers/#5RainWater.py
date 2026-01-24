height = [0,1,0,2,1,0,1,3,2,1,2,1]
main = 0
lefty = []
h = height[0]
for i in height:
    if i > h :
        h = i
    lefty.append(h)


print(lefty)

righty = []
h = height[-1]
for i in range(len(height)-1,-1,-1):
    if height[i] > h :
        h = height[i]
    righty.insert(0,h)
    

print(righty)

l = 0
r = len(height)-1

while l < r:
    main += min(righty[l],lefty[l]) - height[l]
    

    l+=1

print(main)
