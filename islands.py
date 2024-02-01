def traverse_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    paths = []

    def backtrack(row, col, path):
        if row == rows - 1 and col == cols - 1:
            paths.append(path)
            return

        if row < rows - 1:
            backtrack(row + 1, col, path + 'D')

        if col < cols - 1:
            backtrack(row, col + 1, path + 'R')

    backtrack(0, 0, '')
    return paths

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

paths = traverse_matrix(matrix)
for path in paths:
    print(path)
