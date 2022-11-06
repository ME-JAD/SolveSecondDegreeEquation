from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def getTitle(self) -> str:
        pass

    @abstractmethod
    def getCoefficient(self, numCoefficient: int) -> int:
        pass

    @abstractmethod
    def setCoefficient(self, numCoefficient: int, coefficient: float) -> None:
        pass

    @abstractmethod
    def getNumberOfSolutions(self) -> int:
        pass

    @abstractmethod
    def setNumberOfSolutions(self, numberOfSolutions: int) -> None:
        pass

    @abstractmethod
    def getSolution(self, numSolution: int) -> float:
        pass

    @abstractmethod
    def setSolution(self, numSolution: int, solution: float) -> None:
        pass
