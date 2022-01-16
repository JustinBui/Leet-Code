class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        left_moving = len(digits) - 1

        total = digits[left_moving]
        total += 1  # Do the plus one
        carry = 0

        while (True):
            total += carry

            digits[left_moving] = total % 10

            if (total >= 10):
                # Since we need to carry, we must add 1 to the index above the current
                carry = 1

                if (left_moving == 0):   # If it equals 0, we cannot move further left
                    digits.insert(0, 1)
                    break

                left_moving -= 1
            else:
                break

            total = digits[left_moving]

        return digits


if __name__ == "__main__":
    test = Solution()

    arr = [2, 9, 2, 9]
    testOutput = test.plusOne(arr)

    print(testOutput)
