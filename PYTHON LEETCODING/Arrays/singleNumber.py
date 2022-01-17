from mailbox import NoSuchMailboxError
from re import A

from numpy import number


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # hash_list = dict()
        # result = 0

        # for n in nums:
        #     if (n not in hash_list):
        #         hash_list[n] = 1
        #     else:
        #         hash_list[n] += 2

        # for key in hash_list:
        #     if (hash_list[key] == 1):
        #         return key

        # MORE EFFICIENT SOLUTION: https://www.youtube.com/watch?v=krgK0UlfNYY
        def singleNumber(self, nums: list[int]) -> int:
            answer = 0
            for n in nums:
                answer = answer ^ n

            return answer


if __name__ == "__main__":
    test = Solution()
    nums = [1]

    found = test.singleNumber(nums)
    print(found)
