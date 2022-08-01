# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import numpy as np
from Krylow import Krylow
from QRHouseholder import QRMetoda

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #print(np.transpose(np.ones(5)))
    #b = np.reshape(np.ones(5), (5,1))
    #print(b)
    #print(b[0, :])
    #print(b[:,0])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
A = np.array([[2,1], [3,1]])
an = Krylow(A)
print(an)
print(QRMetoda(A, 20))
print()