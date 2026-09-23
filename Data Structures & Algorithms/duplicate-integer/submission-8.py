class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        hashset.update(nums)
        if len(hashset) == len(nums):
            return False
        else:
            return True