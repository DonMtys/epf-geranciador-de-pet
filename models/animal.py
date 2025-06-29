import uuid

class Animal:
    def __init__(self, nome,especie, raca,idade,status='disponível', doador_id=None, fotourl=None , animal_id=None):

        self.id = animal_id or str(uuid.uuid4())

        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade 
        self.status = status
        self.doador_id = doador_id 
        self.fotourl = fotourl

    def marcar_como_adotado(self):
        self.status = 'adotado'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'especie': self.especie,
            'raca': self.raca,
            'idade': self.idade,
            'status': self.status,
            'doador_id': self.doador_id,
            'fotourl': self.fotourl
        }

    
    def __repr__(self): 
        return f"<Animal {self.id} - {self.nome} ({self.especie})>"
