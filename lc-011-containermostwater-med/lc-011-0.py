class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calculateArea(i, j):
            return min(height[i], height[j]) * abs(i-j)
        
        left = 0
        right = len(height)-1 
        max_area = -1

        while left != right:
            area = calculateArea(left, right)
            if area > max_area:
                max_area = area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area