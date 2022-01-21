class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        result = []
        for i in set1:
            if i in set2:
                result.append(i)

        return result


nums1 = [1, 2, 2, 1, 4, 4, 5, 2, 1, 8, 5]
nums2 = [2, 2, 5, 4, 1]

test = Solution()
answer = test.intersection(nums1, nums2)

print(answer)
