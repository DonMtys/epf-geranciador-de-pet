
from bottle import Bottle, template
from services.animal_service import AnimalService

class AnimalController:
    def __init__(self, app: Bottle):
        self.animal_service = AnimalService()
        app.route('/animais', 'GET', self.index)