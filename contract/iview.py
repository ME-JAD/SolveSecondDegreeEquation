from abc import ABC, abstractmethod
from contract.imodel import IModel


class IView(ABC):
    @abstractmethod
    def displayMessage(self, message: str) -> None:
        pass

    @abstractmethod
    def setModel(self, model: IModel) -> None:
        pass

    @abstractmethod
    def askFloat(self) -> float:
        pass

    @abstractmethod
    def displaySolution(self) -> None:
        pass
