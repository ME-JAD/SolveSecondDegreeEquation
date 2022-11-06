from contract.iview import IView
from contract.imodel import IModel


class Controller:
    __model: IModel
    __view: IView

    def __init__(self, model: IModel, view: IView):
        pass

    def start(self):
        pass
