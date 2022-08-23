from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = [mat[0][0]]
        m = len(mat)
        n = len(mat[0])
        total_number_of_elements = m * n
        down = False
        i = 0
        j = 0
        while len(result) < total_number_of_elements:
            if down:
                new_i = i + 1
                new_j = j - 1
            else:
                new_i = i - 1
                new_j = j + 1
            if new_i < 0 or new_i == m or new_j < 0 or new_j == n:
                if down:
                    j += (i == m - 1)
                    i += (i < m - 1)
                else:
                    i += (j == n - 1)
                    j += (j < n - 1)
                # if i < 0 or i == m:
                #     if i < 0:
                #         i += 1
                #     else:
                #         i -= 1

                #     if j ==

                # if j < 0 or j == n:
                #     if j < 0:
                #         j += 1
                #     else:
                #         j -= 1
                down = not down
            else:
                i = new_i
                j = new_j
            # print(mat[i][j])
            result.append(mat[i][j])
        return result


########################################################
class Solution_LC:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        # Check for an empty matrix
        if not matrix or not matrix[0]:
            return []

        # The dimensions of the matrix
        N, M = len(matrix), len(matrix[0])

        # Incides that will help us progress through
        # the matrix, one element at a time.
        row, column = 0, 0

        # As explained in the article, this is the variable
        # that helps us keep track of what direction we are
        # processing the current diaonal
        direction = 1

        # Final result array that will contain all the elements
        # of the matrix
        result = []

        # The uber while loop which will help us iterate over all
        # the elements in the array.
        while row < N and column < M:

            # First and foremost, add the current element to
            # the result matrix.
            result.append(matrix[row][column])

            # Move along in the current diagonal depending upon
            # the current direction.[i, j] -> [i - 1, j + 1] if
            # going up and [i, j] -> [i + 1][j - 1] if going down.
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)

            # Checking if the next element in the diagonal is within the
            # bounds of the matrix or not. If it's not within the bounds,
            # we have to find the next head.
            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:

                # If the current diagonal was going in the upwards
                # direction.
                if direction:

                    # For an upwards going diagonal having [i, j] as its tail
                    # If [i, j + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    row += (
                        column == M - 1
                    )  # this for when we reach the right/left wall at the same time
                    column += (column < M - 1)
                else:

                    # For a downwards going diagonal having [i, j] as its tail
                    # if [i + 1, j] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i, j + 1] becomes the next head
                    column += (
                        row == N - 1
                    )  # this for when we reach the top/bottom wall at the same time
                    row += (row < N - 1)

                # Flip the direction
                direction = 1 - direction
            else:
                row = new_row
                column = new_column

        return result


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans = sol.findDiagonalOrder(mat)
    print(ans)