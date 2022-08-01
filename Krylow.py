# coding=utf-8
import math
import numpy as np
A = np.array([1,3])
#reusing, a co
def Gauss_L(L, b):#działą
    if b.size!=L.shape[0]:
        print("Niewłaściwe dane 2")
        return
    x = b.copy()
    for i in range(0, b.size):
        for j in range(0, i):
            x[i] -= L[i][j]*x[j]
    return x
def Gauss_U(U, b):
    if b.size!=U.shape[0]:
        print("Niewłaściwe dane 2")
        return
    x = b.copy()
    #print(x)
    zakres = range(0, b.size)
    for i in zakres[::-1]:#odwrót
        zak2 = range(i+1, b.size)#+1 musi być
        for j in zak2[::-1]:
            x[i] -= U[i][j]*x[j]

        x[i] /= U[i][i]
        #print(x, f'tak przez {U[i][i]}')
    return x
def Doolittle(A):
    l = np.zeros(np.shape(A))
    u = np.zeros(np.shape(A))
    for i in range(0, np.shape(A)[0]):
                l[i][i] = 1
    #        elif i < j:
    #            l[i][j] = 0
    #        else:
    #           u[i][j] = 0
    # u pierwszy wiersz
    u[0][:] = A[0][:]
    #print(l, '\n', u)
    for j in range(0, np.shape(A)[1]):#najpierw kolumna
        for i in range(0, np.shape(A)[0]):#potem wiersz
            if i > j: #l
                l[i][j] = A[i][j]
                for k in range(0, j):#+1
                    #print(i, j, k)
                    l[i][j] -= l[i][k] * u[k][j]
                l[i][j] /= u[j][j] # to sprawia trudnosc, to najpierw, a co jeśli jj?
                #tak, zamiana jednostek to był klucz
                #dla i=1 j=0
                #l = 1 - (1*1)
                #dla i=2 j=0
                #l = 1 -(l[0]=1*u[0]+l[1]*u[1])=1-(1*1+1
            else: #u
                u[i][j] = A[i][j]
                for k in range(0, i):
                    #print(i, j, k)
                    u[i][j] -= l[i][k] * u[k][j]
        #print(f'{j} ','kolumna zrobiona')
        #print(l, '\n', u)

    #print(l,'\n', u, '\n', print(A==np.dot(l,u)))# stack

    return l, u
def Krylow(A):
    if A.any() == np.empty:
        return
    if np.size(A)<4 :
        return
    if np.ndim(A) != 2 :
        return
    if np.shape(A)[0] != np.shape(A)[1]:
        return
    n = np.shape(A)[0]
    b = np.reshape(np.ones(n), (n,1))
    Up = np.zeros((n,n))
    for i in range(n-1, -1, -1):
        #np.put(U[:, i], b)
        for j in range(0, n):
            Up[j, i] = b[j]
        #U[:,i] = b
        b = np.dot(A, b)
    Y = -b
    # podprzestrzeń Kryłowa utworzona
    #print(Up)
    #print(Y)
    l, u = Doolittle(Up)
    t = Gauss_L(l, Y)
    a = Gauss_U(u, t)
    #print(a)
    ans = np.ones(n+1)
    ans[1:] = a.T
    return ans
#współczynniki od największej potęgi do 0