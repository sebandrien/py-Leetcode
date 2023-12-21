class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0,len(height) - 1
        res = 0

        while left <= right:
            area = min(height[right], height[left]) * (right - left)
            res = max(res, area)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return res
