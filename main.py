from model.model import Model
from view.view import View
from controller.controller import Controller


controller = Controller(Model(), View())
controller.start()
