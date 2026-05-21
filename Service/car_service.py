from dataclasses import dataclass
from Models.car_models import CarResponse, CarCreate
from Repository.car_repository import InMemoryRepository

@dataclass
class CarService:

    car_repo : InMemoryRepository

    def create_car(self, car : CarCreate) -> CarResponse:
        return self.car_repo.create_car(car)

    def get_by_id(self, car_id : int) -> CarResponse:
        return self.car_repo.get_by_id(car_id)