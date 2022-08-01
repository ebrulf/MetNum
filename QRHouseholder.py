# coding=utf-8
import math
import numpy as np
import scipy.linalg as lin
def QRRozkład(A):
    if A.any() == np.empty:
        return
    if np.size(A)<4 :
        return
    if np.ndim(A) != 2 :
        return
    if np.shape(A)[0] != np.shape(A)[1]:
        return
    n = np.shape(A)[0]
    Q = np.identity(n)
    for i in range(0, n):
        a = A[i:,i]
        print("kolumna")
        print(a)
        skal = np.zeros(np.shape(a))
        skal[0] = 1
        v = a-lin.norm(a)*skal
        print(v)
        if lin.norm(v)!=0: #zapomniałem o ostatnim przypadku
            v = v*(1/lin.norm(v))
        H = np.identity(np.size(a))-2*np.outer(v, v)
        print("tymczasowo")
        print(H)
        if i!=0:
            H_temp = np.identity(n)
            for j in range(i, n):
                for k in range(i, n):
                    H_temp[j,k] = H[j-i, k-i]
            H = H_temp
        print(H)
        Q = np.dot(H, Q)
        print("koniec")
    return Q, np.dot(Q.T, A)
def QRMetoda(A, iteracje):
    if A.any() == np.empty:
        return
    if np.size(A)<4 :
        return
    if np.ndim(A) != 2 :
        return
    if np.shape(A)[0] != np.shape(A)[1]: #dla kwadratowych macierzy
        return
    A_temp = A
    for i in range(0, iteracje):
        Qt, Rt = QRRozkład(A_temp)
        A_temp = np.dot(Rt, Qt)
        print("a teraz")
        print(A_temp)
    print(lin.eigvals(A))
    return np.diag(A_temp)