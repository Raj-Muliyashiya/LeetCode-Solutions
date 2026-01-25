class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            new_list[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums )-1,-1,-1):
            new_list[i] *= post
            post *= nums[i]

        return new_list
    
        