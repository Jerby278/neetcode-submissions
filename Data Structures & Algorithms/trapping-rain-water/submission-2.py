class Solution:
    def trap(self, h: List[int]) -> int:
        # using two pointers
        res = 0
        if not h:
            return 0
        l, r = 0, len(h) - 1
        max_left,max_right = h[l], h[r]
        while l < r:
            water_for_this_block = 0
            if max_left <= max_right:
                l+=1
                water_for_this_block = min(max_left, max_right) - h[l]
                max_left = max(max_left,h[l])
            elif max_left > max_right:
                r-=1
                water_for_this_block = min(max_left, max_right) - h[r]
                max_right = max(max_right, h[r])
            if water_for_this_block > 0:
                res += water_for_this_block
        return res