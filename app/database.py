from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import settings  # Importar la configuración
from app.models.user import Base

# Crear el motor de la base de datos
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Crear la fábrica de sesiones
async_session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, autoflush=False, expire_on_commit=False
)


# Función para crear la base de datos y las tablas
async def create_db_and_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Función para obtener una sesión de base de datos
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
