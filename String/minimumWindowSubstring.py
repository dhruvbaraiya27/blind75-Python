class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sIndex = -1
        left=right=0
        min_length = float('inf')
        t_freq = [0] * 128
        n = len(s)
        m = len(t)
        count=0
        
        for c in t:
            t_freq[ord(c)] += 1
        while right < n:
            c = s[right]
            if t_freq[ord(c)] > 0:
                count +=1
            t_freq[ord(c)]-=1
            while count == m:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    sIndex = left
                j = s[left]
                t_freq[ord(j)] +=1
                if t_freq[ord(j)] > 0:
                    count -=1
                left +=1
            right +=1
        return "" if sIndex==-1 else s[sIndex: sIndex+min_length]

            



