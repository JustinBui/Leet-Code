class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        res = []

        def backtrack(i, subset, s):
            if s == target:
                res.append(subset[::])
                return
            if i >= len(candidates) or s > target:
                return

            subset.append(candidates[i])
            backtrack(i + 1, subset, s + candidates[i])

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, subset, s)

        backtrack(0, [], 0)
        return res


if __name__ == '__main__':
    obj = Solution()

    candidates = [2, 5, 2, 1, 2]
    target = 5

    print(obj.combinationSum2(candidates=candidates, target=target))
