import uuid 
from datetime import datetime

class Adocao:
    def __init__(self, animal_id , adotante_id, data_adocao=None, adocao_id=None):
        self.id = adocao_id if adocao_id is not None else str(uuid.uuid4())
        self.animal_id = animal_id
        self.adotante_id = adotante_id
        self.data_adocao = data_adocao if data_adocao is not None else datetime.now().isoformat()
        self.status = 'pendente'

        def confimar(self):
            self.status = 'aprovada'
        def rejeitar(self):
            self.status = 'rejeitada'
        def to_dict(self):
            return {
                'id': self.id,
                'animal_id': self.animal_id,
                'adotante_id': self.adotante_id,
                'data_adocao': self.data_adocao,
                'status': self.status
            }
        def __repr__(self):
            return f"<Adocao {self.id} - Animal {self.animal_id} adotante {self.adotante_id} em {self.data_adocao} - Status: {self.status}>"


