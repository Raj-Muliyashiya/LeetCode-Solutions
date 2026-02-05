class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        i = 0
        max_len = 0

        for j in range(len(s)):
            
            dic[s[j]] = dic.get(s[j],0)+1
            max_char = max(dic.values())
            current_len = j-i+1

            if current_len - max_char > k :
                dic[s[i]] -= 1
                i += 1

            max_len = max(max_len,j-i+1)

        return max_len
        