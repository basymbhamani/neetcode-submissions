class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = dict()
        for n in nums:
            occurrences[n] = occurrences.get(n, 0) + 1
        res = []
        for i in range(k):
            biggest = max(occurrences, key=occurrences.get)
            res.append(biggest)
            del occurrences[biggest]
        return res