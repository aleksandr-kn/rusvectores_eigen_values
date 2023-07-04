import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
import sys

# Читает вектора из файла в numpy array, его же возвращает
def readVectorsToNPArray(path):
    list = []
    with open(path, mode="r", encoding="utf-8") as file:
        for item in file:
            vector = item.rstrip().split(' ')[1::]
            list.append(vector)
    return np.array(list,dtype=float)

# Вычисляет собственные значения переданной матрицы
def getEigenValues(A):
    # вектор среднего по всем строкам X
    meanVector = np.mean(A, axis=0)

    # Вычитаем meanVector из каждой строки матрицы X
    centeredA = A - meanVector

    transposedA = centeredA.transpose()

    resultMatrix = transposedA.dot(centeredA)

    eigs = np.linalg.eigvalsh(resultMatrix)
    # Оставляем только действительные собственные числа
    # realEigs = np.real(eigs[np.isreal(eigs)])
    # Сортируем по убыванию значений
    sortedEigs = np.sort(eigs)[::-1]
    return sortedEigs

# Визуализация собстенных значений матрицы
def plotEigenValues(values, title):
    indexes = np.arange(len(values))
    # Plot the array values
    plt.scatter(indexes, values, s=5)

    # Set labels and title
    plt.xlabel('Номер')
    plt.ylabel('Значения собственных чисел')
    plt.title(title)

    # Display the plot
    plt.show()

if __name__ == '__main__':
    if (not sys.argv[1]):
        sys.exit('Укажите путь до списка векторов')
    path = str(sys.argv[1])

    title = 'График собственных чисел'
    if (sys.argv[2]):
        title = str(sys.argv[2])  

    A = readVectorsToNPArray(path)
    eigenValues = getEigenValues(A)
    plotEigenValues(eigenValues, title)