import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def readVectorsToNPArray(path):
    list = []
    with open(path, mode="r", encoding="utf-8") as file:
        for item in file:
            vector = item.rstrip().split(' ')[1::]
            list.append(vector)
    return np.array(list,dtype=float)

def getEigenValues(A):
    transposedA = A.transpose()
    resultMatrix = transposedA.dot(A)
    eigs = linalg.eigvals(resultMatrix)
    # Оставляем только действительные собственные числа
    realEigs = np.real(eigs[np.isreal(eigs)])
    # Сортируем по убыванию значений
    sortedEigs = np.sort(realEigs)[::-1]
    return sortedEigs

def plotEigenValues(values):
    indexes = np.arange(len(values))
    # Plot the array values
    plt.scatter(indexes, values, s=5)

    # Set labels and title
    plt.xlabel('Номер')
    plt.ylabel('Значения собственных чисел')
    plt.title('Банк')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    A = readVectorsToNPArray('./vectors/ruscorpora_upos_skipgram_300_5_2018/banks.txt')
    eigenValues = getEigenValues(A)
    plotEigenValues(eigenValues)

