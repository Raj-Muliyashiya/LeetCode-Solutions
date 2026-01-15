strs = ['neet', 'code']

new_strs = ''

for i in strs:
    new_strs += str(len(i)) +"#"+i

print(new_strs)
    


new_list = []
i = 0

while i < len(new_strs):
    j = i
    while new_strs[j] != '#':
        j+=1
    length = int(new_strs[i:j])
    print(length)
    i = j+1
    j = i + length
    new_list.append(new_strs[i:j])
    i=j

print(new_list)