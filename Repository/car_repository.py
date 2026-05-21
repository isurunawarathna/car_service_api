from datetime import datetime
from Models.car_models import CarResponse, CarCreate
from typing import Dict, Optional

class CarServiceError(Exception):
    pass

class InMemoryRepository:

    def __init__(self):
        self.__cars : Dict[int, CarResponse] = {}
        self.__count : int = 1

    def create_car(self, car : CarCreate) -> CarResponse:

        car_obj = CarResponse(
            id=self.__count,
            maker=car.maker,
            model=car.model,
            year=car.year,
            car_type=car.car_type,
            fuel_type=car.fuel_type,
            rate_per_km=car.rate_per_km,
            milage=car.milage,
            license_plate=car.license_plate,
            created_at= datetime.now().isoformat(),
            updated_at= datetime.now().isoformat()
        )

        self.__cars[self.__count] = car_obj
        self.__count += 1
        return car_obj

    def get_by_id(self, car_id : int) -> Optional[CarResponse]:
        return self.__cars.get(car_id)










