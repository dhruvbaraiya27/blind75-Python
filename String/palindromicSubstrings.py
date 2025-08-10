class Solution:
    def expand(self, s:str, left: int, right: int) -> int:
        cnt=0
        while left >=0 and right < len(s) and s[left]==s[right]:
            cnt +=1
            left -=1
            right +=1
        return cnt

    def countSubstrings(self, s: str) -> int:
        n= len(s)
        if n < 2:
            return n
        ans =0
        for i in range(n):
            ans += self.expand(s,i,i)
            ans += self.expand(s,i,i+1)
        return ans
