class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = s.replace(" ","")
        new_str = ""

        for i in s:
            if i.isalnum() == True:
                new_str += i

        l = 0
        r = len(new_str) -1

        while l < r:
            if new_str[l] != new_str[r]:
                return False
            elif new_str[l] == new_str[r]:
                l+=1
                r-=1
        return True