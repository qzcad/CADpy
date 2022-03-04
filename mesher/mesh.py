from abc import ABC, abstractmethod
from typing import List

from mesher.element import Element
from mesher.node import Node


class Mesh(ABC):
    """
    The interface for meshes
    """
    @abstractmethod
    def nodes_number(self) -> int:
        pass

    @abstractmethod
    def nodes(self) -> List[Node]:
        pass

    @abstractmethod
    def node(self, node_id: int) -> Node:
        pass

    @abstractmethod
    def elements_number(self) -> int:
        pass

    @abstractmethod
    def elements(self) -> List[Element]:
        pass

    @abstractmethod
    def element(self) -> Element:
        pass


class MeshFabric(ABC):
    """
    The interface for mesh generation algorithms
    """
    @abstractmethod
    def build(self) -> Mesh:
        pass
