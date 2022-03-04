from abc import ABC, abstractmethod
from typing import List

from mesher.node import Node


class Element(ABC):
    """
    The interface for elements
    """

    @abstractmethod
    def id(self) -> int:
        """
        The method returns the integer identifier of the element

        :return: the integer identifier of the element
        """
        pass

    @abstractmethod
    def nodes_number(self) -> int:
        """
        This method returns the number of nodes in the element

        :return: the number of nodes in the element
        """
        pass

    @abstractmethod
    def nodes(self) -> List[Node]:
        """
        This method returns the list of nodes incident to the element

        :return: the list of nodes incident to the element
        """
        pass

    @abstractmethod
    def measure(self) -> float:
        """
        This method calculates a dimensional measure of the (one-, two-, and three-dimensional) element

        :return: the measure of the element
        """
        pass


class ElementSizeException(Exception):
    """
    The class of the exception for the cases when the number of values isn't the same to the number of nodes in the element
    """
    pass
