from fastapi import FastAPI
from Routers.car_routers import router as car_router

app = FastAPI(title="Sri Lankan Car Service API")

app.include_router(car_router)

