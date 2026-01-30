s = "pwwkew"
count = 0
left = 0
hash_set = set()
for right in range(len(s)):
    while s[right] in hash_set:
        hash_set.remove(s[left])
        left += 1
    hash_set.add(s[right])
    count = max(count,len(hash_set))


print(count)



        