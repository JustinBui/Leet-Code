class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = dict()

        for n in nums:
            if counts.get(n) != None:
                return True
            else:
                counts[n] = 1

        return False


if __name__ == "__main__":
    s = Solution()

    s.containsDuplicate([1, 2, 3, 1])
