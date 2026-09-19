class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [None] * length
        prefix = [None] * length
        postfix = [None] * length
        prefix[0] = 1
        for i in range(1, length):
            prefix[i] = prefix[i-1] * nums[i-1]
        z = length - 1
        postfix[z] = 1
        for i in range(z-1, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        for i in range(length):
            res[i] = postfix[i] * prefix[i]
        return res
        