from numpy import random
import numpy as np
import math as m


def generar_desarreglo(n):
    arreglo = np.arange(n) + 1

    for i in range(n - 1):
        j = np.random.randint(i + 1, n)

        arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

    if arreglo[-1] == n - 1:
        arreglo[-1], arreglo[-2] = arreglo[-2], arreglo[-1]

    return arreglo


def generate_unsorted(n, k, file):
    with open(file, 'a') as f:
        for i in range(k):
            arr = generar_desarreglo(n)
            f.write(','.join(map(str, arr)) + '\n')


def generate_sorted(n, k, file):
    arr = np.array([i + 1 for i in range(n)])
    with open(file, 'a') as f:
        for i in range(k):
            f.write(','.join(map(str, arr)) + '\n')


def generate_rev_sorted(n, k, file):
    arr = np.array([i + 1 for i in range(n)][::-1])
    with open(file, 'a') as f:
        for i in range(k):
            f.write(','.join(map(str, arr)) + '\n')


def generate_nearly_sorted(n, k, file):
    with open(file, 'a') as f:
        for i in range(k):
            arr = np.array([i + 1 for i in range(n)])

            # Swap 10%-25% of the elements
            for j in range(int(random.uniform(0.1, 0.25) * n)):
                idx1 = random.randint(0, n)
                idx2 = random.randint(0, n)
                arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

            f.write(','.join(map(str, arr)) + '\n')


def generate_dataset(fun, file, n=5, k=30):
    # How much arrays from 10 to 10**n with an step of s
    lim = 10 ** n
    i = 10

    # I need to generate k arrays of size from 10 to 10**n in even steps

    while i < lim:
        print(f"n={i}")
        step = (i*10 - i) / k
        l = i
        c=0
        while l <= i*10:
            print(f"{c+1}/{k}")
            fun(l, 1, file)
            l += step
            l = m.ceil(l)
            c+=1

        i *= 10


print("Generating datasets...")
print("Unsorted")
generate_dataset(generate_unsorted, '/home/marcor/CLionProjects/tarea1-INF221/ordenamiento/data/unsorted.txt', 5, 30)

print("Sorted")
generate_dataset(generate_sorted, '/home/marcor/CLionProjects/tarea1-INF221/ordenamiento/data/sorted.txt', 5, 30)

print("Reverse Sorted")
generate_dataset(generate_rev_sorted, '/home/marcor/CLionProjects/tarea1-INF221/ordenamiento/data/rev_sorted.txt', 5, 30)

print("Nearly Sorted")
generate_dataset(generate_nearly_sorted, '/home/marcor/CLionProjects/tarea1-INF221/ordenamiento/data/nearly_sorted.txt', 5, 30)


