import csv
from typing import List

from matplotlib import pyplot as plt


def read_measurement(name: str, offset: int = 0) -> List[float]:
    with open("wyniki.csv", newline="") as f:
        reader = csv.reader(f)
        for line in reader:
            if line[0] == name:
                return [float(item) for item in line[1 + offset:]]


if "__main__" == __name__:
    elements = read_measurement("name")
    szukanie_iteracyjne = read_measurement("Szukanie iteracyjne")
    polowkowe = read_measurement("Szukanie połówkowe")
    szukanie_w_bst = read_measurement("Szukanie w drzewie BST")
    szukanie_w_avl = read_measurement("Szukanie w drzewie AVL")

    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas wykonania w sekundach)')
    plt.title('Porównanie Sa(n) Sb(n) Sta(n) Stb(n)')

    # plt.plot(elements, szukanie_iteracyjne)
    plt.plot(elements, polowkowe)
    plt.plot(elements, szukanie_w_bst)
    plt.plot(elements, szukanie_w_avl)

    # plt.legend(["Szukanie iteracyjne", "Szukanie połówkowe", "Szukanie w drzewie BST", "Szukanie w drzewie AVL"])
    plt.legend(["Szukanie połówkowe", "Szukanie w drzewie BST", "Szukanie w drzewie AVL"])
    plt.show()
