class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False  # Eliminate base case

        counts = dict()
        for letter in s:
            if counts.get(letter) == None:
                counts[letter] = 1
            else:
                counts[letter] += 1

        counts2 = dict()
        for letter in t:
            if counts2.get(letter) == None:
                counts2[letter] = 1
            else:
                counts2[letter] += 1

        if counts == counts2:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()

    print(sol.isAnagram("anagram", "nagaram"))
