from typing import List

from mesher.node import Node


class Node2D(Node):
    def __init__(self, x: float, y: float, node_id: int):
        self._x = x
        self._y = y
        self._id = node_id

    @property
    def id(self) -> int:
        return self._id

    def dim(self) -> int:
        return 2

    def coordinates(self) -> List[float]:
        return [self._x, self._y]

    @id.setter
    def id(self, node_id: int):
        self._id = node_id

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, v: float):
        self._x = v

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, v: float):
        self._y = v
