class Solution:
    def palindromeAfterDeletion(self, s:str, ptr1: int, ptr2: int) -> bool:
        while ptr1 <= ptr2:
            if s[ptr1] == s[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s) - 1
        deletions = 0

        while ptr1 <= ptr2:
            if s[ptr1] == s[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            else: # not matching
                if (ptr1 + 1) != ptr2: # not adjacent
                    return self.palindromeAfterDeletion(s, ptr1, ptr2 - 1) or self.palindromeAfterDeletion(s, ptr1 + 1, ptr2)

                else: # they are adjacent
                    return True
        return True
