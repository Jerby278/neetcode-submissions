class Solution:
    def productExceptSelf(self, Input: list[int]) -> list[int]:
        result = [1] * (len(Input))
        prefix_num = 1
        for i in range(len(Input)):
            result[i] = prefix_num
            prefix_num *= Input[i]
        postfix_num = 1
        for i in range(len(Input) - 1, -1, -1):
            result[i] *= postfix_num
            postfix_num *= Input[i]
        return result