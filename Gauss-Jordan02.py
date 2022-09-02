from numpy import matrix, linalg
import numpy as np

print("For 'A * X = B' we need to write as 'I * X = S'")

matrix_A = np.array([[2.0, 1.0, 1.0],[0.30, 2.0, 0.25],[1.0, 1.0, 2.0]])

print('matrix_A')
print(matrix_A)

matrix_B = np.array([[39.0],[13.0],[45.0]])

print('matrix_B')
print(matrix_B)

print("Knowing that 'A * A_inv = I', the solution comes down to 'S = A_inv * B'")

matrix_A_inv = linalg.inv(matrix_A)
print(matrix_A_inv)

matrix_S = np.matmul(matrix_A_inv, matrix_B)
print('matrix_S')
print(matrix_S)