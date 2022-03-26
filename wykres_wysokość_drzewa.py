from matplotlib import pyplot as plt

from wykres import read_measurement

if "__main__" == __name__:
    elements = read_measurement("name")
    tree_height = read_measurement("Wysokość drzewa BST")
    tree_height_avl = read_measurement("Wysokość drzewa AVL")

    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas wykonania w sekundach')
    plt.title('Wysokość drzew BST i AVL')

    plt.plot(elements, tree_height)
    plt.plot(elements, tree_height_avl)

    plt.legend(["Wysokośc drzewa BST", "Wysokość drzewa AVL"])
    plt.show()
