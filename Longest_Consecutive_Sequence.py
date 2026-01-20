class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_streak = 0

        for num in hashset:
            if (num-1) not in hashset:
                current = num
                current_streak = 1

                while (current+1) in hashset:
                    current += 1
                    current_streak +=1
                max_streak = max(max_streak , current_streak)
        
        return max_streak
        