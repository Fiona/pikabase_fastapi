from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class ElementType(Model):
    id = fields.IntField(pk=True)
    slug = fields.CharField(max_length=255)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return f" {self.name} ({self.slug})"

    class PydanticMeta:
        exclude = ("id",)


ElementType_Pydantic = pydantic_model_creator(ElementType, name="ElementType")
ElementTypeIn_Pydantic = pydantic_model_creator(
    ElementType, name="ElementTypeIn", exclude_readonly=True
)
