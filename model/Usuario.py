from typing import Optional
from pydantic import BaseModel
from .Gasto import Gasto

class Usuario(BaseModel):
    id: int
    nombre: str
    presupuesto: Optional[float] = 0.0
    listaGastos: list = []
    
    def addGasto(self, gasto: Gasto):
        self.listaGastos.append(gasto)