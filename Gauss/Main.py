import numpy as np
from MyException import InputException


def Gauss_sol(A, b):
    if len(A) != len(A[0]) or len(A) != len(b):
        raise InputException('Incorrect dimension')
    M = A[:]
    c = b[:]
    n = len(M)
    indices = np.zeros(n)
    for i in range(n):
        K = np.nonzero(M[i])[0]
        if not len(K):
            if b[i] != 0:
                raise InputException("The system is controversial and hasn't solution")
            else:
                raise InputException("The system has infinite set of solutions")
        else:
            k = K[0]
            for j in filter(lambda a, b=i: a != b, range(0, n)):
                d = M[j][k] / M[i][k]
                c[j] -= float(c[i]) * d
                M[j] -= M[i] * d
            indices[i] = k
    x = np.zeros(n)
    for i in range(n):
        k = int(indices[i])
        x[i] = c[int(indices[i])] * np.sign(M[i][k])
    return x


if __name__ == "__main__":
    fIn = open(r'input')
    fOut = open('output', "w")
    L = fIn.readlines()
    fIn.close()
    listArray = []
    for l in L[:-1]:
        a = l.rstrip().split()
        arr = np.asarray(a, dtype=float)
        listArray.append(arr)
    A = np.asarray(listArray)
    y = np.asarray(L[-1].split(), dtype=float)
    try:
        x = Gauss_sol(A, y)
    except InputException as IE:
        print(IE.message, file=fOut)
    else:
        print(x, file=fOut)
    fOut.close()
