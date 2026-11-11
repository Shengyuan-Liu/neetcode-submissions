class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = sorted(freq.items(), key=lambda a: a[1])[-k:]
        return [item[0] for item in result]