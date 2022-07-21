class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = dict()

        # Keeping track of counts of all unique values
        for n in nums:
            if counts.get(n) == None:
                counts[n] = 1
            else:
                counts[n] += 1

        # Creating buckets (array) of n + 1 elements ranged from [0, n]
        # (n = size of nums array)
        frequency = [[] for i in range(len(nums) + 1)]
        for val, cnt in counts.items():
            frequency[cnt].append(val)

        topK = list()
        for bucket in range(len(frequency) - 1, 0, -1):
            for f in frequency[bucket]:
                topK.append(f)

                if len(topK) == k:
                    return topK


if __name__ == '__main__':
    # entity = {1: 4, 5: 6, 34: 43, 43: 4, 0: 9}

    # entity2 = list(entity.items())

    # print(entity2)

    # print(entity2[0:2][0])

    s = Solution()
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2

    print(s.topKFrequent(nums, k))
