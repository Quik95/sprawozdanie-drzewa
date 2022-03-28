from matplotlib import pyplot as plt

from wykres import read_measurement

if "__main__" == __name__:
    elements = read_measurement("name")
    tworzenie_tablicy_b = read_measurement("Tworzenie tablicy B")
    tworzenie_drzewa_BST = read_measurement("Budowanie drzewa BST")
    tworzenie_drzewa_AVL = read_measurement("Budowanie drzewa AVL")

    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas wykonania w sekundach)')
    plt.title('Porównanie tworzenie tablicy B, tworzenie drzewa BST i tworzenie drzewa AVL')

    plt.plot(elements, tworzenie_tablicy_b)
    plt.plot(elements, tworzenie_drzewa_BST)
    plt.plot(elements, tworzenie_drzewa_AVL)

    plt.legend(["Tworzenie tablicy B", "Budowanie drzewa BST", "Budowanie drzewa AVL"])
    plt.show()
