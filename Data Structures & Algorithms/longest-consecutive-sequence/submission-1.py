class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        sortedNums = sorted(nums)
        maxStep = 1
        step = 1
        for i in range(len(sortedNums) - 1):
            if sortedNums[i + 1] == sortedNums[i]:
                continue
            if sortedNums[i + 1] == sortedNums[i] + 1:
                step += 1
                maxStep = max(step, maxStep)
            else:
                step = 1
        maxStep = max(step, maxStep)
        return maxStep