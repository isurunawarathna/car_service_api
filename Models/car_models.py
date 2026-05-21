from enum import Enum
from typing import Optional
from pydantic import BaseModel
from pydantic import Field
from datetime import datetime


class CarTypes(str,Enum):
    SEDAN = "Sedan"
    HATCHBACK = "Hatchback"
    VAN = "Van"
    LORRY = "Lorry"
    SUV = "suv"

class FuelType(str, Enum):
    PETROL = "Petrol",
    DIESEL = "Diesel",
    ELECTRIC = "Electric",
    HYBRID = "Hybrid"

class CarBase(BaseModel):
    maker : str = Field(...,min_length=1,max_length=60,description="Car Manufacturer")
    model : str = Field(...,min_length=1,max_length=50,description="Car Model")
    year : int = Field(...,ge=2000,description="Manufactured Year")
    car_type : CarTypes = Field(description="Type of Car")
    fuel_type : FuelType = Field(description="Type of Fuel")
    rate_per_km : float = Field(...,ge=0,le=1000,description="Rate Per Kilometer")
    milage : float = Field(ge=0,description="Milage of the Vehicle")
    license_plate : str = Field(description="License Plate Number")

class CarCreate(CarBase):
    pass

class CarResponse(CarBase):
    id: int
    created_at : str
    updated_at : Optional[str] = None


