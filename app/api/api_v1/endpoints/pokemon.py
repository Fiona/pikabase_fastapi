from typing import Any, List

from fastapi import APIRouter, Path
from tortoise.exceptions import DoesNotExist

from app.models.elementtypes import ElementType
from app.models.pokemon import Pokemon, Pokemon_Pydantic, PokemonIn_Pydantic
from app.responses import error_response_404, error_response_422

router = APIRouter()


def build_pokemon_from_orm_object(obj):
    return Pokemon_Pydantic(
        number_national=obj.number_national,
        name=obj.name,
        slug=obj.slug,
        element_1=obj.element_1.slug,
        element_2=None if not obj.element_2 else obj.element_2.slug
    )


@router.get("/", response_model=List[Pokemon_Pydantic])
async def get_all_pokemon():
    return [
        build_pokemon_from_orm_object(p)
        for p in
        await Pokemon.all().prefetch_related("element_1", "element_2")
    ]


@router.post(
    "/", response_model=Pokemon_Pydantic,
    responses={**error_response_422}
)
async def create_pokemon(pokemon: PokemonIn_Pydantic):
    pokemon_data = pokemon.dict(exclude_unset=True)
    try:
        pokemon_data['element_1'] = await ElementType.get(slug=pokemon_data['element_1_slug'])
        if "element_2_slug" in pokemon_data:
            pokemon_data['element_2'] = await ElementType.get(slug=pokemon_data['element_2_slug'])
    except DoesNotExist:
        raise DoesNotExist("elementtype does not exist.")
    new_obj = await Pokemon.create(**pokemon_data)
    return await Pokemon_Pydantic.from_tortoise_orm(new_obj)


@router.get(
    "/{slug}", response_model=Pokemon_Pydantic,
    responses={**error_response_404, **error_response_422}
)
async def get_pokemon(slug: str = Path(..., title="Slug of a pokemon to get i.e. bulbasaur")):
    return build_pokemon_from_orm_object(
        await Pokemon.get(slug=slug).prefetch_related("element_1", "element_2")
    )
