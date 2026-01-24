class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        new_list = []

        for i in range(len(nums)):
            if nums[i] > 0 :
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1
            while l < r :
                total = nums[i] + nums[l] + nums[r]
                if total > 0 :
                    r -= 1
                if total < 0 :
                    l += 1
                if total == 0:
                    new_list.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return new_list        