class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max  # swap if negative

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            ans = max(ans, curr_max)

        return ans
        
