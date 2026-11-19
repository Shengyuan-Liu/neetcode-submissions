class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1          # 保证 nums1 更短
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            L1 = nums1[i-1] if i > 0 else float('-inf')
            R1 = nums1[i]   if i < m else float('inf')
            L2 = nums2[j-1] if j > 0 else float('-inf')
            R2 = nums2[j]   if j < n else float('inf')
            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2:
                    return max(L1, L2)
                return (max(L1, L2) + min(R1, R2)) / 2
            elif L1 > R2:
                hi = i - 1
            else:
                lo = i + 1