from typing import List

import numpy as np

from mesher.element import Element, ElementSizeException
from mesher.node import Node
from mesher.node2d import Node2D


class Triangle2D(Element):
    def __init__(self, nodes: List[Node2D], element_id: int):
        self._nodes = nodes
        self._id = element_id
        if len(nodes) != 3:
            raise ElementSizeException("The number of nodes is not equal 3")

    @property
    def id(self) -> int:
        return self._id

    def nodes_number(self) -> int:
        return 3

    def nodes(self) -> List[Node]:
        return self._nodes

    def measure(self) -> float:
        a = np.array(self._nodes[0].coordinates())
        b = np.array(self._nodes[1].coordinates())
        c = np.array(self._nodes[2].coordinates())
        ab = np.linalg.norm(b-a)
        bc = np.linalg.norm(c-b)
        ca = np.linalg.norm(a-c)
        s = 0.5 * (ab + bc + ca)
        return np.sqrt(s * (s - ab) * (s - bc) * (s - ca))

    @id.setter
    def id(self, element_id: int):
        self._id = element_id
