class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        max_length=0
        start=0
        n = len(s)
        for end, ch in enumerate(s):
            if ch in map and map[ch] >= start:
                start = map[ch]+1
            map[ch] = end
            max_length = max(max_length, end - start +1)

        return max_length
