import collections

class Solution:
    # ---------------------------- BRUTE FORCE O(n^3) ----------------------------
    # def isPalindrome(self, s: str) -> bool:
    #     l, r = 0, len(s) - 1
    #     while l <= r:
    #         if s[l] != s[r]:
    #             return False
    #         l += 1
    #         r -= 1
        
    #     return True

    # def countPalindromicSubsequence(self, s: str) -> int:
    #     palindromes_found = 0
    #     all_palindromes = []

    #     for a in range(0, len(s)):
    #         for b in range(a+1, len(s)):
    #             for c in range(b+1, len(s)):
    #                 candidate = s[a] + s[b] + s[c]         
    #                 if self.isPalindrome(candidate):
    #                     if candidate not in all_palindromes:
    #                         palindromes_found += 1
    #                         all_palindromes.append(s[a] + s[b] + s[c])
        
    #     return palindromes_found
    # ------------------------------------------------------------------------------------

    # Optimal solution using hash maps O(26 * n) = O(n)
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        res = set()
        right = collections.Counter(s)

        for i in range(len(s)):
            right[s[i]] -= 1 # s[i] will no longer be on the right of index i (Taking it off hash map)
            if right[s[i]] == 0:
                right.pop(s[i])
            
            for j in 'abcdefghijklmnopqrstuvwxyz': # Looping through each letter of alphabet
                if j in left and j in right: # Check if valid palindrome. Ex: 'aba' where a's are on left and right and b is at i
                    res.add(j + s[i] + j)

            left.add(s[i]) # All elements on the left of i will now be part of the set left
        
        return len(res)


if __name__ == '__main__':
    s = 'adc'

    entity = Solution()
    print(entity.countPalindromicSubsequence(s))