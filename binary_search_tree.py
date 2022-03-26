import time
from dataclasses import dataclass
from functools import wraps
from typing import Optional, List, Tuple, Any


@dataclass
class DrzewoBST:
    root: int
    left: Optional['DrzewoBST']
    right: Optional['DrzewoBST']

    def get_height(self) -> int:
        left_height = -1 if self.left is None else self.left.get_height()
        right_height = -1 if self.right is None else self.right.get_height()
        return max(left_height, right_height) + 1

    def to_list_pre_order(self, res: List[int] = None) -> List[int]:
        if res is None:
            res = []
        res.append(self.root)
        if self.left is not None:
            self.left.to_list_pre_order(res)
        if self.right is not None:
            self.right.to_list_pre_order(res)
        return res

    def find(self, needle: int) -> int:
        if self.root == needle:
            return needle
        if needle < self.root:
            return self.left.find(needle)
        else:
            return self.right.find(needle)

    @staticmethod
    def from_list(tablica: List[int]) -> 'DrzewoBST':
        drzewo = DrzewoBST(root=tablica[0], left=None, right=None)

        for item in tablica[1:]:
            target = drzewo
            while True:
                if item < target.root:
                    if target.left is None:
                        target.left = DrzewoBST(root=item, left=None, right=None)
                        break
                    else:
                        target = target.left
                else:
                    if target.right is None:
                        target.right = DrzewoBST(root=item, left=None, right=None)
                        break
                    else:
                        target = target.right

        return drzewo
