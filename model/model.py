from contract.imodel import IModel


class Model(IModel):
    __title: str
    __coefficients: [int]
    __numberOfSolutions: int
    __solutions: [int]
    
    def __init__(self):
        pass

    def getTitle(self) -> str:
        pass

    def getCoefficient(self, numCoefficient: int) -> int:
        pass

    def setCoefficient(self, numCoefficient: int, coefficient: float) -> None:
        pass

    def getNumberOfSolutions(self) -> int:
        pass

    def setNumberOfSolutions(self, numberOfSolutions: int) -> None:
        pass

    def getSolution(self, numSolution: int) -> float:
        pass

    def setSolution(self, numSolution: int, solution: float) -> None:
        pass
