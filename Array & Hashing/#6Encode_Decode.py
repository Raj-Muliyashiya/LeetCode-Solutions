class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""

        for i in strs:
            new_string += str(len(i))+'#'+i

        return new_string


    def decode(self, s: str) -> List[str]:
        new_list = []

        i=0
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            new_list.append(s[start : end])

            i = end

        return new_list 


