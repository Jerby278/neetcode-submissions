class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current = 0
        l,r = 0, 0
        while current < len(arr)-1:
            maxx = max(arr[current:])
            r = arr.index(maxx, current)
            while l<r:
                arr[l] = maxx
                l+=1
            current = r+1
        if len(arr) > 1:

            arr[-2] = arr[-1]
        arr[-1] = -1
        
        return arr