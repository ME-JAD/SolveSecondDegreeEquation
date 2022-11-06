from contract.imodel import IModel
from contract.iview import IView


class View(IView):
    def __init__(self):
        pass

    def displayMessage(self, message: str) -> None:
        pass

    def getModel(self) -> IModel:
        pass

    def setModel(self, model: IModel) -> None:
        pass

    def askFloat(self) -> float:
        pass

    def displaySolution(self) -> None:
        pass
