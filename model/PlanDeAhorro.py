from typing import Optional
from pydantic import BaseModel

class PlanDeAhorro(BaseModel):
    meta: float
    ahorro: float
    duracion: int
    frecuencia: int
    progreso: int = 0;
    descripcion: Optional[str] = None