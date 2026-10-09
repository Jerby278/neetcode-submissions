class Solution:
    def removeElement(self, nums: List[int], value: int) -> int:
        try:
            while True:
                nums.remove(value)
        except:
            return len(nums)