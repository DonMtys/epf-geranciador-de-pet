from bottle import route, template
from services.animal.service import AnimalService


class AnimalController:
    def __init__(self):
        self.animal_service = AnimalService()
        route('/animais', 'GET', self.index)

    def index(self):
        lista_de_animais = self.animal_service.get_all()
        return template('animais_lista', animals=lista_de_animais)