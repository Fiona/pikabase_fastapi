from typing import Optional

from pydantic import BaseModel
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.elementtypes import ElementType


class Pokemon(Model):
    id = fields.IntField(pk=True)
    number_national = fields.IntField()
    slug = fields.CharField(max_length=255)
    name = fields.CharField(max_length=255)
    element_1 = fields.ForeignKeyField("models.ElementType", related_name="pokemon_with_element_1")
    element_2 = fields.ForeignKeyField("models.ElementType", related_name="pokemon_with_element_2", null=True)

    def __str__(self):
        return f"#{self.number_national} {self.name} ({self.slug})"

    class PydanticMeta:
        exclude = ("id",)


class Pokemon_Pydantic(BaseModel):
    number_national: int
    slug: str
    name: str
    element_1: Optional[str]
    element_2: Optional[str]

    class Config:
        orm_mode = True

"""
PokemonIn_Pydantic = Pokemon_Pydantic
"""


#Pokemon_Pydantic = pydantic_model_creator(Pokemon, name="Pokemon")
PokemonIn_Pydantic = pydantic_model_creator(
    Pokemon, name="PokemonIn", exclude_readonly=True
)
