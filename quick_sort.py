from typing import List

def quick_sort(dane: List[int], lo: int = 0, hi: int = None) -> List[int]:
    if hi is None:
        hi = len(dane) - 1

    if lo >= hi:
        return

    j = partition(dane, lo, hi)

    quick_sort(dane, lo, j)
    quick_sort(dane, j+1, hi)

def partition(dane: List[int], lo: int, hi: int) -> int:
    p = dane[(lo + hi) // 2]
    i = lo - 1
    j = hi + 1
    while True:
        while True:
            i += 1
            if dane[i] >= p:
                break
        while True:
            j -= 1
            if dane[j] <= p:
                break
        if i >= j:
            break
        dane[i], dane[j] = dane[j], dane[i]
    return j