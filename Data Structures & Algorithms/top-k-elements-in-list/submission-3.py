class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)


        hashc = defaultdict(list)
        mostfrequent = []
        for num, freq in counts.items():

            hashc[freq].append(num)

        for i in reversed(sorted(hashc)):
            for j in hashc[i]:
                if k > 0:
                    mostfrequent.append(j)
                    k -= 1
        return mostfrequent
