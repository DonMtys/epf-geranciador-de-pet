from bottle import Bottle, template
from services.animal_servico import AnimalService 

class AnimalController:
    def __init__(self, app: Bottle):
        self.animal_service = AnimalService()
        app.route('/animais', 'GET', self.index)
    
    def index(self):
        animais = self.animal_service.get_all() 
        return template('animais/index', animais=animais)