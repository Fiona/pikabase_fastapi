from tortoise.contrib.fastapi import register_tortoise

from app.config import TORTOISE_CONFIG
from app.app import app


register_tortoise(
    app,
    config=TORTOISE_CONFIG,
    generate_schemas=True,
)
