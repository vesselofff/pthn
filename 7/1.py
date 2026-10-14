def load_matrix(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        matrix = [list(map(int, line.split())) for line in f if line.strip()]

    if not matrix:
        return matrix

    first_len = len(matrix[0])
    return matrix if all(len(row) == first_len for row in matrix) else False


result = load_matrix("matrix.txt")
print(result)          
