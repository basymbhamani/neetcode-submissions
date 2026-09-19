class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for i in range(k):
            max_key = max(count, key=count.get)
            res.append(max_key)
            count.pop(max_key) 

        return res