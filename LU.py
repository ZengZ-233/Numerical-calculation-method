import numpy as np


def L1U(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U


if __name__ == '__main__':
    A = np.array([[3,2,1], [2,5,9], [1,9,17]])
    L, U = L1U(A)
    print("L:")
    print(L)
    print("U:")
    print(U)
