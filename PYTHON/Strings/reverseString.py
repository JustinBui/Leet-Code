class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Using 2-pointer approach
        first, second = 0, len(s) - 1

        while(first < second):
            # Swapping values of the 2 iterators
            s[first], s[second] = s[second], s[first]
            first += 1
            second -= 1


if __name__ == "__main__":
    s = ["H", "a", "n", "n", "a", "h"]
    test = Solution()

    test.reverseString(s)
    print(f"After: {s}")
