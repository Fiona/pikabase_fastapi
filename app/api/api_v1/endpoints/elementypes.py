from typing import Any, List

from fastapi import APIRouter, Path
from tortoise.query_utils import Q

from app.models.elementtypes import ElementType, ElementType_Pydantic, ElementTypeIn_Pydantic
from app.models.pokemon import Pokemon, Pokemon_Pydantic
from app.api.api_v1.endpoints.pokemon import build_pokemon_from_orm_object
from app.responses import error_response_404, error_response_422

router = APIRouter()


@router.get("/", response_model=List[ElementType_Pydantic])
async def get_elementtypes():
    return await ElementType_Pydantic.from_queryset(ElementType.all())


@router.post(
    "/", response_model=ElementType_Pydantic,
    responses={**error_response_422},
)
async def create_elementtype(elementtype: ElementTypeIn_Pydantic):
    new_obj = await ElementType.create(**elementtype.dict(exclude_unset=True))
    return await ElementType_Pydantic.from_tortoise_orm(new_obj)


@router.get(
    "/{slug}", response_model=ElementType_Pydantic,
    responses={**error_response_404, **error_response_422},
)
async def get_elementtype(slug: str = Path(..., title="Slug of an elementtype to get i.e. grass")):
    return await ElementType_Pydantic.from_queryset_single(ElementType.get(slug=slug))


@router.get(
    "/{slug}/pokemon", response_model=List[Pokemon_Pydantic],
    responses={**error_response_404, **error_response_422},
    description="Gets all pokemon that are of a particular element type"
)
async def get_elementtype_pokemon(slug: str = Path(..., title="Slug of an elementtype to get i.e. grass")):
    elementtype = await ElementType.get(slug=slug)
    pokemon = await Pokemon.filter(
        Q(element_1=elementtype) | Q(element_2=elementtype)
    ).prefetch_related("element_1", "element_2")
    return [build_pokemon_from_orm_object(p) for p in pokemon]

