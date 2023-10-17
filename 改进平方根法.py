import numpy as np

def LD(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    D = np.zeros(n)
    for i in range(n):
        D[i] = A[i, i] - np.dot(L[i, :i] ** 2, D[:i])
        L[i, i] = 1.0
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i] * L[i, :i], D[:i])) / D[i]
    return L, D

if __name__ == '__main__':
    A = np.array([[3, 3, 5], [3, 5, 9], [5, 9, 17]])
    L, D = LD(A)
    print("L:")
    print(L)
    print("D:")
    print(D)
