from dataclasses import dataclass
from typing import Optional, List


@dataclass
class DrzewoAVL:
    root: int
    left: Optional['DrzewoAVL']
    right: Optional['DrzewoAVL']

    @staticmethod
    def from_sorted_list(data: List[int], start: int = 0, end: int = None) -> Optional['DrzewoAVL']:
        if end is None:
            end = len(data) - 1

        if start > end:
            return None

        middle = (start + end) // 2
        drzewo = DrzewoAVL(
            root=data[middle],
            left=DrzewoAVL.from_sorted_list(data, start=start, end=middle - 1),
            right=DrzewoAVL.from_sorted_list(data, start=middle + 1, end=end),
        )

        return drzewo

    def to_list_pre_order(self, res: List[int] = None) -> List[int]:
        if res is None:
            res = []
        res.append(self.root)
        if self.left is not None:
            self.left.to_list_pre_order(res)
        if self.right is not None:
            self.right.to_list_pre_order(res)
        return res

    def get_height(self) -> int:
        left_height = -1 if self.left is None else self.left.get_height()
        right_height = -1 if self.right is None else self.right.get_height()
        return max(left_height, right_height) + 1

    def find(self, needle: int) -> int:
        if self.root == needle:
            return needle
        if needle < self.root:
            return self.left.find(needle)
        else:
            return self.right.find(needle)
