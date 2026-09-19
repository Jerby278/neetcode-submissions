class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []

        for x in strs:
            issorted = tuple(sorted(x))
            hashmap[issorted].append(x)

        for value in hashmap.values():
            result.append(value)
        return result
        

        