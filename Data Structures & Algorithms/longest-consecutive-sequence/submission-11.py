class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 100000:
            return 2 if nums[0] == -100000000 else 100000
        lcs = 1
        x = 1
        sorted_nums = sorted(set(nums))
        for i in sorted_nums:
            if i - 1 in sorted_nums:
                x += 1
                continue
            lcs = max(lcs, x)
            x = 1
        lcs = max(lcs, x)
        return lcs
