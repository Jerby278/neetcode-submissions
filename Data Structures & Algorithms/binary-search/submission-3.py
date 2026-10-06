class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_i,right_i = 0,len(nums)-1
        while  left_i <=right_i:
            mid = left_i+((right_i-left_i) // 2)
            if nums[mid] > target: #if true: target is within first half of nums
                right_i = mid-1
            elif nums[mid] < target:
                left_i = mid+1
            else: return mid
        return -1