from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = [matrix[0][0]]
        lower_end = 0
        higher_end = len(matrix) - 1

        left_end = 0
        right_end = len(matrix[0]) - 1
        total_number_of_elements = (higher_end + 1) * (right_end + 1)
        direction = "right"
        i = 0
        j = 0
        while len(result) < total_number_of_elements:
            if direction == "right":
                new_i = i
                new_j = j + 1
            elif direction == "left":
                new_i = i
                new_j = j - 1
            elif direction == "down":
                new_i = i + 1
                new_j = j
            elif direction == "up":
                new_i = i - 1
                new_j = j

            ### check for bound

            if new_i < lower_end and direction == "up":
                new_i = lower_end
                # lower_end += 1

                direction = "right"
                print("over bound for down")
                i = new_i
                j = new_j

            elif new_i > higher_end and direction == "down":
                new_i = higher_end
                higher_end -= 1

                direction = "left"
                print("over bound for up")
                i = new_i
                j = new_j

            elif new_j < left_end and direction == "left":
                new_j = left_end
                left_end += 1

                direction = "up"
                print("over bound for left")
                i = new_i
                j = new_j

            elif new_j > right_end and direction == "right":
                new_j = right_end
                right_end -= 1
                lower_end += 1

                direction = "down"
                print("over bound for right")
                i = new_i
                j = new_j
            else:
                i = new_i
                j = new_j
                result.append(matrix[i][j])
            # result.append(matrix[new_i][new_j])
        return result


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rs = sol.spiralOrder(matrix)
    print(rs)