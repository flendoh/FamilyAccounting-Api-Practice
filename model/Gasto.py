from typing import Optional
from pydantic import BaseModel

class Gasto(BaseModel):
    nombre: str
    precio: float
    cantidad: int
    descripcion: Optional[str] = None