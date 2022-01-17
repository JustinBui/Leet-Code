class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums_list = []
        for n in nums:
            if n in nums_list and nums_list.count(n) == 2:
                nums_list = list(filter(lambda a: a != n, nums_list))
            else:
                nums_list.append(n)
        return nums_list[0]


if __name__ == "__main__":
    nums = [0, 1, 0, 1, 0, 1, 99]

    solution = Solution()
    find = solution.singleNumber(nums)
    print(find)
