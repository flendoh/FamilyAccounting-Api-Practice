from typing import Optional
from typing import List
from pydantic import BaseModel
from .Gasto import Gasto

class Usuario(BaseModel):
    id: int
    nombre: str
    presupuesto: Optional[float] = 0.0
    listaGastos: List[Gasto] = []
    
    def addGasto(self, gasto: Gasto):
        self.listaGastos.append(gasto)