from fastapi import APIRouter, status, HTTPException
from Models.car_models import CarResponse, CarCreate
from Repository.car_repository import InMemoryRepository, CarServiceError
from typing import List

from Service.car_service import CarService

router = APIRouter(prefix="/cars",tags=["cars"])
car_service = CarService(car_repo=InMemoryRepository())

@router.post("/",response_model=CarResponse, status_code=status.HTTP_201_CREATED)
def create_car(car : CarCreate) -> CarResponse:
    try:
        return car_service.create_car(car)
    except CarServiceError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

@router.get("/id/{car_id}", response_model=CarResponse, status_code=status.HTTP_302_FOUND)
def get_by_id(car_id : int):
    try:
        return car_service.get_by_id(car_id)
    except CarServiceError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@router.get("/all_cars",response_model=List[CarResponse], status_code=status.HTTP_302_FOUND)
def get_all()->List[CarResponse]:
    try:
        return car_service.get_all()
    except CarServiceError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))



