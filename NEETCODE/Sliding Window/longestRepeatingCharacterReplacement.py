class Solution:
    # Helper function
    def findHighestFreq(self, d: dict) -> int:
        h = 0
        for k, v in d.items():
            h = max(v, h)
        return h

    def characterReplacement(self, s: str, k: int) -> int:
        frequency_hash = dict()
        l, res = 0, 0

        highest_frequency = 0  # Highest frequency of repeating characters within the substring
        for r in range(len(s)):
            # Keeping track of amount of words
            if frequency_hash.get(s[r]) == None:
                frequency_hash[s[r]] = 1
            else:
                frequency_hash[s[r]] += 1

            # Getting the potential highest frequency
            highest_frequency = max(highest_frequency, frequency_hash[s[r]])

            # Validating if this is a valid substring: i.e if the number of possible
            # spaces to fill is <= k, then this substring is valid
            length = r - l + 1

            # Sliding our window if our substring is not valid
            # Valid window: Now take its length and compare it to the current highest length
            if length - highest_frequency <= k:
                res = max(res, length)
            else:
                frequency_hash[s[l]] -= 1
                # Finding the new max frequency in case if max frequency updated as result of shifting our left pointer
                highest_frequency = self.findHighestFreq(frequency_hash)
                l += 1

        return res


if __name__ == '__main__':
    sol = Solution()

    s = "AABABBA"
    k = 1

    print(sol.characterReplacement(s, k))
