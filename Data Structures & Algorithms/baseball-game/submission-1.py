class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = []
        for index,value in enumerate(operations):
            if value == "+":
                stck.append(stck[-1] + stck[-2])
            elif value == "C":
                stck.pop(-1)
            elif value == "D":
                stck.append(stck[-1]*2)
            else:
                stck.append(int(value))
    
        return sum(stck)