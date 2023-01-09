class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) < 4 or len(s) > 12: # Strings that are too big or too small to even make an IP address
            return []

        res = []

        def backtrack(i, dots, current_IP):
            if i == len(s) and dots == 4: # Valid IP Address using all elements of s is generated
                res.append(current_IP[:-1])
                return
            if dots > 4:
                return
            
            for j in range(i, min(len(s),i + 3)):
                # If current digit (substring of s) is between [0, 255] and current digit has no leading 0's
                candidate = s[i:j+1]
                if int(candidate) <= 255 and (len(candidate) == 1 or candidate[0] != '0'):
                    backtrack(j+1, dots+1, current_IP + candidate + '.')
        
        backtrack(i=0, dots=0, current_IP='')
        return res


if __name__ == '__main__':
    s = "25525511135"
    entity = Solution()

    print(entity.restoreIpAddresses(s))