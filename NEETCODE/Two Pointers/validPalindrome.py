class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1

        while (left < right):
            # Ignoring characters that are not alphanumeric
            while (s[left].isalnum() == False) and (left < right):
                left += 1
            while s[right].isalnum() == False and (left < right):
                right -= 1

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    s = "racecar"
    sol = Solution()
    res = sol.isPalindrome(s)

    print(res)
