class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if len(t) > len(s): return ""

        # need freq
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        required = len(need)
        formed = 0
        window = {}
        l = 0
        best_len, best_l = float("inf"), 0

        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                formed += 1

            while formed == required:
                if (r - l + 1) < best_len:
                    best_len = (r - l + 1)
                    best_l = l

                left_c = s[l]
                window[left_c] -= 1
                if left_c in need and window[left_c] < need[left_c]:
                    formed -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_l: best_l + best_len]
