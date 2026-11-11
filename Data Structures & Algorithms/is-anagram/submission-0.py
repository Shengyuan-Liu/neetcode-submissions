class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hash_str(s: str):
            result = {}
            for ch in s:
                result[ch] = result.get(ch, 0) + 1
            return result

        s_table = hash_str(s)
        t_table = hash_str(t)
        return s_table == t_table
            