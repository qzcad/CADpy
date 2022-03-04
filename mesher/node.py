from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    """
    The interface of the node
    """
    @abstractmethod
    def id(self) -> int:
        """
        The method returns the integer identifier of the node

        :return: the integer identifier of the node
        """
        pass

    @abstractmethod
    def dim(self) -> int:
        """
        The method returns the dimension of the node

        :return: the dimension of the node
        """
        pass

    @abstractmethod
    def coordinates(self) -> List[float]:
        """
        The method returns coordinates of the node as a list of floats

        :return: coordinates of the node
        """
        pass
