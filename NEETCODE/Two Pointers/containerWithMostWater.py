class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            candidate_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, candidate_area)

            # When advancing out left and right pointers, we want to maximize
            # the height
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:  # both heights equal, so just move any of the pointers
                left += 1

        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(height))
