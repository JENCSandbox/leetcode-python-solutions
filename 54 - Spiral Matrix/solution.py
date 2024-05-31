from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        spiral_array = []
        rows, cols = len(matrix), len(matrix[0])
        visited = set()

        d, i, j = 0, 0, 0

        while len(visited) != rows*cols:
            spiral_array.append(matrix[i][j])
            visited.add((i, j))

            (dr, dc) = directions[d]
            new_i, new_j = i+dr, j+dc
            if (new_i, new_j) not in visited and new_i in range(rows) and new_j in range(cols):
                i, j = new_i, new_j
            else:
                d = d + 1 if d + 1 in range(len(directions)) else 0
                (dr, dc) = directions[d]
                i, j = i + dr, j + dc
        return spiral_array


sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder([[1,2],[3,4]]))