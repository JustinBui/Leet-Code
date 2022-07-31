class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, curr_array, total):
            # --------------------- Base cases ---------------------
            if total == target:
                res.append(curr_array.copy())  # Valid array, so append
                return
            elif index >= len(candidates) or total > target:
                return  # Invalid array, so do NOT append, just return

            # --------------------- Recursive cases ---------------------

            # Include the current element that index points to in candidates array
            # As you iterate down the decision tree, keep including candidates[index]
            curr_array.append(candidates[index])
            dfs(index, curr_array, total + candidates[index])

            # Do NOT include candidates[index], as you traverse down decision tree,
            # never include that value again. Get new values by passing in index + 1
            curr_array.pop()
            dfs(index + 1, curr_array, total)

        dfs(0, [], 0)

        return res
