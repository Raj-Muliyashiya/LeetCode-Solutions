class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            if nums_set is None:
                nums_set.add(i)
            elif i in nums_set:
                return True
            else:
                nums_set.add(i)
        return False
        