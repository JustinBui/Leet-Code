class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        # Base case:
        if len(nums) == 1:
            return [nums[:]]

        # Recursive case
        for i in range(len(nums)):
            # Choosing the path down decision tree to exclude the number I just popped
            n = nums.pop(0)
            permutations = self.permute(nums)

            for p in permutations:
                p.append(n)

            # Adding multiple arrays (Representing Permutations) into result
            res.extend(permutations)
            # Placing the value we just popped back into the array
            nums.append(n)

        return res


if __name__ == '__main__':
    obj = Solution()

    n = [1, 2, 3]
    print(obj.permute(n))
