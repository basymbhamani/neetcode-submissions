class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        res = []

        for n in nums[0:len(nums)-1]:
            prefix.append(prefix[-1] * n)

        for i in range(len(nums)-1):
            postfix.append(postfix[-1] * nums[-1-i])

        for i in range(len(nums)):
            res.append(prefix[i]*postfix[-1-i])

        return res