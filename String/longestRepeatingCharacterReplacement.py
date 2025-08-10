class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        start=0
        max_length=0
        max_freq = 0
        freq = [0] * 26
        for end in range(n):
            idx = ord(s[end]) - ord('A')
            freq[idx] +=1
            max_freq = max(max_freq, freq[idx])
            while (end - start + 1) - max_freq > k: 
                freq[ord(s[start]) - ord('A')]-=1
                start +=1
            max_length = max(max_length, (end - start + 1))
        return max_length
