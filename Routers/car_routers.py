

from fastapi import APIRouter, status, HTTPException
from Models.car_models import CarResponse, CarCreate
from Repository.car_repository import InMemoryRepository, CarServiceError

from Service.car_service import CarService

router = APIRouter(prefix="/cars",tags=["cars"])
car_service = CarService(car_repo=InMemoryRepository())

@router.post("/",response_model=CarResponse, status_code=status.HTTP_201_CREATED)
def create_car(car : CarCreate) -> CarResponse:
    try:
        return car_service.create_car(car)
    except CarServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

