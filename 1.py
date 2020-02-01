import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def Shaker(A):  # Shaker
    for i in range(0, int (len(A)/2)):
        for j in range(i, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
            for j in range(len(A) - 2 - i, i + 1):
                if A[j] < A[j - 1]:
                    a = A[j]
                    A[j] = A[j - 1]
                    A[j - 1] = a


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a




table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Shaker"])
x = []
y1 = []
y2 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    # print(A)

    B = A.copy()
    # print(B)

    #BubbleSort(A)
    print("---")
    # print(A)

    #QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    Shaker(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Shaker   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()
