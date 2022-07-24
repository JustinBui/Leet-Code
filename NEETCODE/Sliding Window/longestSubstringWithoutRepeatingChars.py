from enum import unique


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        leftmost = 0
        longest_length = 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[leftmost])
                leftmost += 1

            longest_length = max(longest_length, r - leftmost + 1)
            visited.add(s[r])

        return longest_length


if __name__ == '__main__':
    sol = Solution()

    s = "dvdf"
    print(sol.lengthOfLongestSubstring(s))

    # a b c c d a k j h u y
