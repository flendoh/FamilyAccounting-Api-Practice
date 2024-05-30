from typing import Optional
from pydantic import BaseModel
from .PlanDeAhorro import PlanDeAhorro

class Familia(BaseModel):
    id: int
    nombreFamilia: Optional[str] = None
    cabezaFamilia: int = None
    listaMiembros: Optional[list] = []
    listaPlanDeAhorro: Optional[list] = []
        
    def addMiembro(self, id_member: int):
        self.listaMiembros.append(id_member)
    
    def addPlanDeAhorro(self, plan: PlanDeAhorro):
        self.listaPlanDeAhorro.append(plan)