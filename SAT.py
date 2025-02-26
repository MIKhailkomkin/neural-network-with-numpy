import numpy as np
class MatrixOperations:
    def determinant(self, matrix):
        if len(matrix) == 1:
            return matrix[0][0]  # Определитель 1×1 матрицы — это сам элемент
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  # Формула для 2×2 матрицы

        det = 0
        for col in range(len(matrix)):
            minor = [row[:col] + row[col + 1:] for row in matrix[1:]]  # Удаляем первую строку и текущий столбец
            det += ((-1) ** col) * matrix[0][col] * self.determinant(minor)  # Вызов через self
        return det

    def mull(self, A, B):
        if len(A[0]) != len(B):  # Проверка корректности умножения
            raise ValueError("Количество столбцов A должно совпадать с количеством строк B")

        C = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
        return C

    def invert_matrix(self, matrix):

        n = len(matrix)

        identity_matrix = np.eye(n)

        augmented_matrix = np.hstack([matrix, identity_matrix])

        for i in range(n):
            if augmented_matrix[i, i] == 0:
                for j in range(i + 1, n):
                    if augmented_matrix[j, i] != 0:
                        augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                        break

            augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]

            for j in range(n):
                if j != i:
                    augmented_matrix[j] -= augmented_matrix[i] * augmented_matrix[j, i]

        return augmented_matrix[:, n:]

    def SAT(self, S, A, T):
        if self.determinant(S) != 0 and self.determinant(T) != 0:
            S = self.invert_matrix(S)
            tmp_matrix = self.mull(S, A)
            ans = self.mull(tmp_matrix, T)
            return ans
        else:
            print('error')

  
