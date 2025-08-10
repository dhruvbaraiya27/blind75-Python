class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_all=0
        xor_num=0

        for i in range(n+1):
            xor_all ^= i
        for num in nums:
            xor_num ^= num
        return xor_all ^ xor_num
