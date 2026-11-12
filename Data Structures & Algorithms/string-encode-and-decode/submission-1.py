class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            prefix = f"#{length}#"
            result += prefix
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        hash_start = 0
        result = []
        while hash_start < len(s):
            if s[hash_start] == '#':
                hash_end = hash_start + 1
                while s[hash_end] != '#':
                    hash_end += 1
                number_str = int(s[hash_start + 1: hash_end])

                str_start = hash_end + 1
                content = s[str_start: str_start + number_str]
                result.append(content)

                hash_start = str_start + number_str
        return result
