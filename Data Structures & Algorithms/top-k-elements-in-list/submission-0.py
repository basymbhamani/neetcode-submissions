class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        histogram = {}
        for n in nums:
            histogram[n] = histogram.get(n, 0) + 1
        sortedValues = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
        return [t[0] for t in sortedValues[:k]]
