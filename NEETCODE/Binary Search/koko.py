from math import ceil


class Solution:
    # # BRUTE FORCE
    # def minEatingSpeed(self, piles: list[int], h: int) -> int:
    #     k = 0
    #     total_hours = 0

    #     while total_hours != h:
    #         k += 1
    #         total_hours = 0
    #         for p in piles:
    #             total_hours += ceil(p / k)

    #     return k

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # All possible values of k
        l, r = 1, max(piles)
        res = r

        while l <= r:
            total_hours = 0
            k = (l + r) // 2
            for p in piles:
                # Calculating total hours Koko eats at the current k
                total_hours += ceil(p / k)
            # print(f'K={k}, TotalHours={total_hours} == h={h}: {total_hours == h}')
            if total_hours <= h:
                # if Koko is eating too fast, slow down eating rate by considering the lower half
                # of all possible k's array
                r = k - 1

                # In some edge cases, we may not find an EXACT value of total_hours that equals to h.
                # So to cover these edge cases, we can just take the value of k with total_hours that is the NEXT LEAST away from h.
                res = min(res, k)
            elif total_hours > h:
                # Koko is eating too slow, now speed up eating rate by considering upper half
                l = k + 1

        return res


if __name__ == '__main__':
    obj = Solution()

    piles = [312884470]
    h = 312884469
    print(obj.minEatingSpeed(piles, h))
