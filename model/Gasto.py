from typing import Optional
from pydantic import BaseModel

class Gasto(BaseModel):
    categoria: str
    precio: float
    cantidad: int
    descripcion: Optional[str] = None

    def monto(self):
        return self.cantidad*self.precio