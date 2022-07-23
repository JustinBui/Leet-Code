import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        closest_dist = math.inf

        for i, v in enumerate(nums):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                candidate = v + nums[left] + nums[right]
                # We want to minimize distance between target and candidate as much as possible
                distance = abs(target - candidate)

                if distance < closest_dist:
                    closest_dist = distance
                    result = candidate

                if candidate > target:  # Make our candidate smaller to get closer to the target
                    right -= 1
                elif candidate < target:  # Make out candidate larger to get closer to target
                    left += 1
                elif candidate == target:  # Found the EXACT target
                    return result

        return result


if __name__ == '__main__':
    s = Solution()

    nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
    target = -2

    print(f'Output {s.threeSumClosest(nums, target)}')
