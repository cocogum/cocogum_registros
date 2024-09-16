"""
Este módulo configura y ejecuta la aplicación FastAPI.
"""

from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routers import (
    association_router,
    auth_router,
    base_router,
    commerce_router,
    community_router,
    form_router,  # Importar el nuevo router
    knowledge_router,
    role_router,
    user_router,
)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, Any]:
    """
    Context manager para la vida útil de la aplicación.
    """
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get('/')
async def read_root() -> dict[str, str]:
    """
    Endpoint raíz que devuelve un mensaje de bienvenida.
    """
    return {'message': 'Hello World'}


@app.get('/example')
async def read_example() -> dict[str, str]:
    """
    Endpoint de ejemplo que devuelve datos de ejemplo.
    """
    return {'example': 'data'}


@app.get('/users/me')
async def read_current_user() -> dict[str, str]:
    """
    Endpoint que devuelve información del usuario.
    """
    return {'username': 'test@example.com'}


app.include_router(role_router, prefix='/api/v1/roles', tags=['roles'])
app.include_router(user_router, prefix='/api/v1/users', tags=['users'])
app.include_router(auth_router, prefix='/api/v1/auth', tags=['auth'])
app.include_router(
    association_router, prefix='/api/v1/associations', tags=['associations']
)
app.include_router(base_router, prefix='/api/v1/base', tags=['base'])
app.include_router(
    commerce_router, prefix='/api/v1/commerce', tags=['commerce']
)
app.include_router(
    community_router, prefix='/api/v1/community', tags=['community']
)
app.include_router(
    knowledge_router, prefix='/api/v1/knowledge', tags=['knowledge']
)
app.include_router(
    form_router.router, prefix='/forms', tags=['forms']
)  # Incluir el nuevo router
