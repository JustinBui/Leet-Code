class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        it1, it2 = 0, 0

        result = []
        while (it1 < len(nums1) and it2 < len(nums2)):
            # If the iterators point to values that are equal, increment BOTH...
            if (nums1[it1] == nums2[it2]):
                result.append(nums1[it1])
                it1 += 1
                it2 += 1
            # Otherwise, we increment whichever iterator is least
            elif (nums1[it1] < nums2[it2]):
                it1 += 1
            else:   # if nums2[it2] < nums1[it1]
                it2 += 1

        return result


if __name__ == '__main__':
    nums1 = [9, 3, 2, 5, 1]
    nums2 = [9]

    test = Solution()
    answer = test.intersect(nums1, nums2)

    print(answer)
