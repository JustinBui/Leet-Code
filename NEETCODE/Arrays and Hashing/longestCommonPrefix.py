class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Edge case: Automatically return the string if its the only one in our given array
        if len(strs) == 1:
            return strs[0]
        
        longest_prefix = ''
        it = 0 # Iterator of of each string in strs pointing to the current common letter
        keep_looping = True

        while keep_looping:
            if it < len(strs[0]):
                current_letter = strs[0][it]
            else:
                break

            for s in strs:
                if len(s) == 0 or it >= len(s) or current_letter != s[it]:
                    keep_looping = False
                    break
            
            if keep_looping:
                longest_prefix += current_letter
            it += 1

        return longest_prefix

if __name__ == '__main__':
    strs = ["dog","racecar","car"]

    entity = Solution()
    print(entity.longestCommonPrefix(strs))