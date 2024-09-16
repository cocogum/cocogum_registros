from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    first_name: str = Field(..., min_length=1, max_length=120)
    last_name: str = Field(..., min_length=1, max_length=255)
    phone: str = Field(..., pattern=r'^\+?1?\d{9,15}$')  # Validación teléfono


class UserCreate(UserBase):
    username: str = Field(None, min_length=4, max_length=60)
    password: str = Field(..., min_length=8)  # Cambiado a 'password'


class UserUpdate(BaseModel):
    email: EmailStr = None
    first_name: str = Field(None, min_length=1, max_length=120)
    last_name: str = Field(None, min_length=1, max_length=255)
    phone: str = Field(None, pattern=r'^\+?1?\d{9,15}$')  # Validación teléfono
    password: str = Field(None, min_length=8)  # Cambiado a 'password'


class UserDelete(BaseModel):
    id: int


class MyModel(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class User(UserBase):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
