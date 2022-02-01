# Solution: https://www.youtube.com/watch?v=fMSJSS7eO1w


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while (left < right):
            # As i increments from 0 to n - 1, it represents the sub-square's corners we want
            # to rotate.
            # (i represents the distance from the origin point of left, right, top, bottom)
            for i in range(right - left):
                top, bottom = left, right

                ### ROTATING ALGORITHM GOES HERE ###
                temp = matrix[top][left + i]

                # Assigning top-left as bott-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Assigning bott-left as bott-right
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Assigning top-right as bott-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Assigning top-right as temp value (Originally as top-left)
                matrix[top + i][right] = temp

                
            # Shrinking left and right pointers to go together
            # to simulate us going deeper into the next layer
            left += 1
            right -= 1


if __name__ == '__main__':
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    print("BEFORE:")
    for m in matrix:
        print(m)

    test = Solution()
    test.rotate(matrix)

    print("AFTER:")
    for m in matrix:
        print(m)