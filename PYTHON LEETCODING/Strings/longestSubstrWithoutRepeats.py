class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0

        starting_point = 0
        visited = set()

        while (starting_point < len(s)):

            for i in range(starting_point, len(s)):
                if (s[i] not in visited):
                    visited.add(s[i])

                else:
                    starting_point += 1
                    if (len(visited) > longest_length):
                        longest_length = len(visited)
                    visited.clear()

                    break
        return longest_length


test = Solution()
s = "jbpnbwwd"

length = test.lengthOfLongestSubstring(s)
print(length)
