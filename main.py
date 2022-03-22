import random
import timeit
from functools import wraps
import time
from typing import List, Optional


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time_ns()
        result = f(*args, **kw)
        te = time.time_ns()
        print("func:%r took: %f s" % (f.__name__, (te - ts) / 1000000000))
        return result

    return wrap


@timing
def znajdz_b_w_a(tab_b: List[int], tab_a: List[int]):
    wyniki = []
    for b in tab_b:
        for i, a in enumerate(tab_a):
            if b == a:
                wyniki.append(i)


@timing
def znajdz_a_w_b_polowkowo(tab_a: List[int], tab_b: List[int]):
    wyniki = []

    for needle in tab_a:
        start = 0
        end = len(tab_b) - 1
        while start <= end:
            middle = (end + start) // 2
            if tab_b[middle] > needle:
                end = middle - 1
            elif tab_b[middle] < needle:
                start = middle + 1
            else:
                wyniki.append(middle)
                break

@timing
def stworz_tablice_b(tablica_a: List[int]) -> List[int]:
    tb = tablica_a.copy()
    tb.sort()
    return tb


if __name__ == '__main__':
    tablica_a = list(range(1, 100 + 1))
    random.shuffle(tablica_a)

    tablica_b = stworz_tablice_b(tablica_a)
    znajdz_b_w_a(tablica_b, tablica_a)
    znajdz_a_w_b_polowkowo([2, 6, 8, 1, 5, 10, 7, 9, 4, 3], tablica_b)
