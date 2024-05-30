from typing import Optional
from pydantic import BaseModel

class PlanDeAhorro(BaseModel):
    meta: float
    ahorro: float
    duracion: int
    frecuencia: int
    descripcion: Optional[str] = None