import csv
import gc
import os
import random
from timeit import Timer
from typing import List, Any

from binary_search_tree import DrzewoBST
from drzewo_avl import DrzewoAVL
from quick_sort import quick_sort


def benchmark_function(name: str, f: Any) -> float:
    number_of_runs = 200 if "iteracyjne" not in name else 1
    gc.collect()
    time_taken = Timer(f).timeit(number=number_of_runs) / number_of_runs
    print(f"{name}: {time_taken}s")
    return time_taken


def save_measurement(name: str, measurements: List[float]):
    with open("wyniki.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, *measurements])


def find_iteratively(tab_b: List[int], tab_a: List[int]):
    for b in tab_b:
        for i, a in enumerate(tab_a):
            if b == a:
                break  # znalezione


def find_by_bisection(tab_a: List[int], tab_b: List[int]):
    for needle in tab_a:
        start = 0
        end = len(tab_b) - 1
        while start <= end:
            middle = (end + start) // 2
            if tab_b[middle] > needle:
                end = middle - 1
            elif tab_b[middle] < needle:
                start = middle + 1
            elif tab_b[middle] == needle:
                break  # znalezione


def stworz_tablice_b(tablica_a: List[int]) -> List[int]:
    tb = tablica_a.copy()
    quick_sort(tb)
    return tb


def find_all(drzewo: DrzewoBST, tablica: List[int]):
    for item in tablica:
        drzewo.find(item)


if __name__ == '__main__':
    try:
        os.remove("wyniki.csv")
    except FileNotFoundError:
        pass

    steps = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    with open("wyniki.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(["name", *steps])

    benchmark_tablica_b = []
    benchmark_time_iteratively = []
    benchmark_find_bisection = []
    benchmark_find_in_bst = []
    benchmark_budowa_drzewa = []
    benchmark_budowa_drzewa_avl = []
    benchmark_find_in_avl = []
    wysokości_drzewa = []
    wysokości_drzewa_avl = []

    data = list(range(1, steps[-1] + 1))
    random.shuffle(data)
    for step in steps:
        tablica_a = data[:step]

        tablica_b = stworz_tablice_b(tablica_a)
        benchmark_tablica_b.append(
            benchmark_function(f"Tworzenie tablicy B {step}", lambda: stworz_tablice_b(tablica_a)))

        benchmark_time_iteratively.append(
            benchmark_function(f"Szukanie iteracyjne {step}", lambda: find_iteratively(tablica_b, tablica_a)))

        benchmark_find_bisection.append(
            benchmark_function(f"Szukanie połówkowe {step}", lambda: find_by_bisection(tablica_a, tablica_b)))

        drzewo = DrzewoBST.from_list(tablica_a)
        benchmark_budowa_drzewa.append(
            benchmark_function(f"Budowanie drzewa {step}", lambda: DrzewoBST.from_list(tablica_a)))

        benchmark_find_in_bst.append(
            benchmark_function(f"Szukanie w drzewie BST {step}", lambda: find_all(drzewo, tablica_b)))

        auxiliary_table = DrzewoAVL.from_sorted_list(tablica_b).to_list_pre_order()
        drzewo_avl = DrzewoBST.from_list(auxiliary_table)
        benchmark_budowa_drzewa_avl.append(
            benchmark_function(f"Budowa drzewa AVL {step}", lambda: DrzewoBST.from_list(auxiliary_table))
        )

        benchmark_find_in_avl.append(
            benchmark_function(f"Szukanie w drzewie AVL {step}", lambda: find_all(drzewo_avl, tablica_a)))

        wysokości_drzewa.append(drzewo.get_height())
        wysokości_drzewa_avl.append(drzewo_avl.get_height())

    save_measurement("Tworzenie tablicy B", benchmark_tablica_b)
    save_measurement("Szukanie iteracyjne", benchmark_time_iteratively)
    save_measurement("Szukanie połówkowe", benchmark_find_bisection)
    save_measurement("Budowanie drzewa BST", benchmark_budowa_drzewa)
    save_measurement("Budowanie drzewa AVL", benchmark_budowa_drzewa_avl)
    save_measurement("Szukanie w drzewie BST", benchmark_find_in_bst)
    save_measurement("Szukanie w drzewie AVL", benchmark_find_in_avl)
    save_measurement("Wysokość drzewa BST", wysokości_drzewa)
    save_measurement("Wysokość drzewa AVL", wysokości_drzewa_avl)
