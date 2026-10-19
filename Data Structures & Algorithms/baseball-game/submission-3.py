class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = []
        result = 0
        for value in operations:
            if value == "+":
                result += stck[-1] + stck[-2]
                stck.append(stck[-1] + stck[-2])
            elif value == "C":
                result -= stck.pop()
            elif value == "D":
                result += stck[-1]*2
                stck.append(stck[-1]*2)
            else:
                result += int(value)
                stck.append(int(value))
                
        return result