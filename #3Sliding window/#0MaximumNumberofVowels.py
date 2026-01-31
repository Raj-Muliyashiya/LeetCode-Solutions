s = "abciiidef"
k = 3

vowel = {'a','e','i','o','u'}

count = 0
for i in range(k):
    if s[i] in vowel:
        count += 1

max_count = count

left = 0

for right in range(k,len(s)):
    if s[left] in vowel:
        count -= 1
    left +=1

    if s[right] in vowel:
        count += 1
    
    max_count = max(max_count,count)

print(max_count)