class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = len(nums)
        nums = list(dict.fromkeys(nums))
        if len(nums) < b:
            return True
        else :
            return False