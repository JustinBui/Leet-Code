class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            candidate = numbers[left] + numbers[right]
            if candidate == target:
                return [left+1, right+1]
            elif candidate > target:
                right -= 1  # Candidate value is too large, so advance right pointer left to decrease our sum
            elif candidate < target:
                left += 1  # Vice versa if candidate value is too small


if __name__ == '__main__':
    s = Solution()

    numbers = [-1, 0]
    target = -1
    print(s.twoSum(numbers, target))
