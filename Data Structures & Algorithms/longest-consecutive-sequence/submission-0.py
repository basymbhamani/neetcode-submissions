class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        start = [n for n in num_set if n-1 not in num_set]
        max_count = 0
        for n in start:
            count = 1
            i = n
            while i+1 in num_set:
                count += 1
                i += 1
            if count > max_count:
                max_count = count
        return max_count