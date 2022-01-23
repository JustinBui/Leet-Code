class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_sub = s[0]
        current_length = 1
        LENGTH = len(s)

        # Finding potential odd number substrings
        # Length of string must be at least 3 to get an odd length palindrome
        # that is not 1.
        if (LENGTH >= 3):
            for i in range(1, LENGTH - 1):
                mid = i
                left, right = mid - 1, mid + 1

                while(left >= 0 and right < LENGTH):
                    if (s[left] == s[right]):
                        candidate = s[left:right + 1]
                        if (len(candidate) > current_length):
                            longest_sub = candidate
                            current_length = len(candidate)
                    else:
                        break

                    left -= 1
                    right += 1

        # Finding potential even
        if (LENGTH >= 2):
            for i in range(LENGTH - 1):
                left, right = i, i + 1

                while (left >= 0 and right < LENGTH):
                    if (s[left] == s[right]):
                        candidate = s[left:right + 1]
                        if (len(candidate) > current_length):
                            longest_sub = candidate
                            current_length = len(candidate)
                    else:
                        break

                    left -= 1
                    right += 1

        return longest_sub


if __name__ == '__main__':
    test = Solution()

    s = "bab"
    print(test.longestPalindrome(s))
