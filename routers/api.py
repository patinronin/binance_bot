from fastapi import APIRouter
from routers import home_routes, crypto_currencies_routes
api_router = APIRouter()


api_router.include_router(
    home_routes.router,
    tags=["Home"],
)

api_router.include_router(
    crypto_currencies_routes.router,
    tags=["Crypto currencies"],
)