from typing import Optional
from pydantic import BaseModel
from .Gasto import Gasto

class Usuario(BaseModel):
    id: int
    listaGastos: list = []
    nombre: str

    def addGasto(self, gasto: Gasto):
        self.listaGastos.append(gasto)