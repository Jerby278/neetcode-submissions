class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        res = 0
        for i in nums:
            if i == 1:
                counter+=1
            else:
                res = max(counter,res)
                counter = 0
        res = max(counter, res)
        return res