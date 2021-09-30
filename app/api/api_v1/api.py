from fastapi import APIRouter

from app.api.api_v1.endpoints import pokemon
from app.api.api_v1.endpoints import elementypes

api_router = APIRouter()
api_router.include_router(elementypes.router, prefix="/elementtypes", tags=["elementtypes"])
api_router.include_router(pokemon.router, prefix="/pokemon", tags=["pokemon"])
