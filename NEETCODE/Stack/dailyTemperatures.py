
# --------------------------------------------- BRUTEFORCE O(N^2) ---------------------------------------------
# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         res = list()

#         for t in range(len(temperatures)):
#             days_to_wait = 0
#             current_temp = temperatures[t]
#             warmer_found = False  # If the current day has any warmer days ahead

#             for d in range(t + 1, len(temperatures)):
#                 days_to_wait += 1
#                 if temperatures[d] > current_temp:
#                     warmer_found = True
#                     break

#             if warmer_found == False:
#                 res.append(0)
#             else:
#                 res.append(days_to_wait)

#         return res


# -------------------------------------------- OPTIMIZED APPROACH: Monotonic Stack (NeetCode) -------------------------------------
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Stack keeps track of tuple pairs: (value, index) of temeratures array
        stack = []
        res = [0] * len(temperatures)

        for t in range(len(temperatures)):

            # Checking the top of the stack to see any values less than current value of temperatures[t].
            # NOTE: The stack must NOT be empty to check the top of stack.
            while (len(stack)) > 0 and stack[-1][0] < temperatures[t]:
                # For any values on the stack less than temperatures[t], pop that value until you find a value
                # on the stack that is greater.
                stack_top_val, stack_top_ind = stack.pop()

                # Result at the same index from tuple of stack gets the number of days til a warmer weather
                res[stack_top_ind] = t - stack_top_ind

            stack.append((temperatures[t], t))

        return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    obj = Solution()
    print(obj.dailyTemperatures(temperatures))
