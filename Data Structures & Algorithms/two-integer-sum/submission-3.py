class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = dict()
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in index_dict.keys():
                return [index_dict[num2], i]
            index_dict[num1] = i