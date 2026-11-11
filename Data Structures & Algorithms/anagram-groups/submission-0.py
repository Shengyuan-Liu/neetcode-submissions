class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def reorder(s: str):
            return ''.join(sorted(list(s)))

        table = {}
        for s in strs:
            reordered_s = reorder(s)
            if reordered_s not in table:
                table[reordered_s] = [s]
            else:
                table[reordered_s].append(s)
        return list(table.values())