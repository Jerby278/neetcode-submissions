class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        topKFrequen = []
        counter = 0
        for i, x in sorted(count.items(), key=lambda x: x[1], reverse=True):
            if counter == k:
                return topKFrequen
            topKFrequen.append(i)
            counter += 1

        return topKFrequen
