class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strs = list()
        for i in range(len(strs)):
            sorted_strs.append(''.join(sorted(strs[i])))

        anagrams = dict()

        for j in range(len(sorted_strs)):
            if anagrams.get(sorted_strs[j]) == None:
                anagrams[sorted_strs[j]] = list()

            anagrams[sorted_strs[j]].append(strs[j])

        result = list()
        for key in anagrams:
            result.append(anagrams[key])

        return result


if __name__ == '__main__':
    s = Solution()

    arr = s.groupAnagrams(['a'])
    print(arr)
