class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        
        s1_freq = {}
        for s in s1:
            s1_freq[s] = s1_freq.get(s, 0) + 1
        s1_len = len(s1)

        s2_freq = {}
        for i in range(s1_len):
            s2_freq[s2[i]] = s2_freq.get(s2[i], 0) + 1
        if s2_freq == s1_freq:
            return True

        for i in range(1, len(s2) - s1_len + 1):
            s2_freq[s2[i - 1]] -= 1
            if s2_freq[s2[i - 1]] == 0:
                del s2_freq[s2[i - 1]]
            s2_freq[s2[i + s1_len - 1]] = s2_freq.get(s2[i + s1_len - 1], 0) + 1
            if s2_freq == s1_freq:
                return True

        return False

