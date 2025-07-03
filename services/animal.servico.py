# Ficheiro: services/animal_service.py
import json
from models.animal import Animal 
from config import Config

class AnimalService:
    def __init__(self):
        self.file_path = Config.DATA_PATH / 'animals.json'

    def _load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_data(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_all(self):
        data = self._load_data()
        return [Animal(**animal_data) for animal_data in data]
