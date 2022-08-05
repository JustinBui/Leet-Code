class Solution:
    # Helper function to perform binary serach for each row of the matrix
    def binarySearch(self, row: list, target: int) -> bool:
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        first_row = 0
        last_row = len(matrix) - 1

        # An element at RIGHT_INDEX (For each row) is guaranteed to be larger than an element at LEFT_INDEX
        LEFT_INDEX = 0
        RIGHT_INDEX = len(matrix[0]) - 1

        while first_row <= last_row:
            mid_row = (first_row + last_row) // 2

            if target >= matrix[mid_row][LEFT_INDEX] and target <= matrix[mid_row][RIGHT_INDEX]:
                # Target found in bound from a particular row (As each element per row is in ascending order)
                return self.binarySearch(matrix[mid_row], target)
            elif target > matrix[mid_row][RIGHT_INDEX]:
                first_row = mid_row + 1
            elif target < matrix[mid_row][LEFT_INDEX]:
                last_row = mid_row - 1

        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7]]
    target = 7

    obj = Solution()
    print(obj.searchMatrix(matrix, target))
