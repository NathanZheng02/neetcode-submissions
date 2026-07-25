class Solution:

    def encode(self, strs: List[str]) -> str:
        build_a_str = ""
        for s in strs:
            build_a_str = build_a_str + str(len(s)) + "ඞ" + s
        return build_a_str
    def decode(self, s: str) -> List[str]:
        build_a_list = []
        idx = 0
        while idx < len(s):
            end = idx
            while s[end] != "ඞ":
                end += 1
            length = int(s[idx:end])
            idx = end + 1
            end = idx + length
            build_a_list.append(s[idx:end])
            idx = end
        return build_a_list
