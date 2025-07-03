
from bottle import Bottle
from .user_controller import UserController
from .animal_controller import AnimalController



def init_controllers(app: Bottle):
    print("-> Inicializando UserController...")
    user_controller = UserController(app)

    print("-> Inicializando AnimalController...")
    animal_controller = AnimalController(app)
    