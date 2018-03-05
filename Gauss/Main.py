import numpy as np
from MyException import InputException


def Gauss_sol(A, B):
    if len(A) != len(A[0]) or len(A) != len(B):
        raise InputException('Incorrect dimension')
    M = A.copy()
    C = B.copy()
    n = len(M)
    indices = np.zeros(n)
    for i in range(n):
        K = np.nonzero(M[i])[0]
        if not len(K):
            if B[i] != 0:
                raise InputException("The system is controversial and hasn't solution")
            else:
                raise InputException("The system has infinite set of solutions")
        else:
            k = K[0]
            for j in filter(lambda a: a != i, range(0, n)):
                d = M[j][k] / M[i][k]
                C[j] -= C[i] * d
                M[j] -= M[i] * d
            indices[i] = k
    for i in range(n):
        C[i] *= np.sign(M[i][i])
    return C


def inverse(A):
    d = np.linalg.det(A)
    if 0.001 > d >= 0:
        raise InputException("Inverse matrix doesn't exist")
    B = np.identity(len(A))
    return Gauss_sol(A, B)


def condition_number(A, B):
    A1 = inverse(A)
    a = np.max(np.sum(np.abs(A), axis=0))
    a1 = np.max(np.sum(np.abs(A1), axis=0))
    return a * a1


def get_matrix(L, l, r):
    listArray = []
    for i in range(l, r, 1):
        a = L[i].rstrip().split()
        arr = np.asarray(a, dtype=float)
        listArray.append(arr)
    return np.asarray(listArray)


if __name__ == "__main__":
    fIn = open(r'input')
    fOut = open('output', "w")
    L = fIn.readlines()
    n = len(L[0].rstrip().split())
    fIn.close()
    A = get_matrix(L, 0, n)
    y = get_matrix(L, n, len(L))
    F = object
    if not len(y):
        F = condition_number
    else:
        y = y[0]
        F = Gauss_sol
    try:
        x = F(A, y)
    except InputException as IE:
        print(IE.message, file=fOut)
    else:
        print(x, file=fOut)
    fOut.close()
