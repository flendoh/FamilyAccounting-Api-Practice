from typing import Dict
from typing import List
from typing import Optional
from datetime import datetime
from collections import defaultdict
from .Familia import Familia
from .Usuario import Usuario
from .Gasto import Gasto

class Reporte:
    def __init__(self, familia: Familia, listaUsuarios: List[Usuario]):
        self.id_familia: int = familia.id
        self.nombre_familia: Optional[str] = familia.nombreFamilia
        self.presupuesto_total: float = 0

        for cabeza in listaUsuarios:
            if familia.cabezaFamilia == cabeza.id:
                self.cabeza_familia: Usuario = cabeza
                self.presupuesto_total += cabeza.presupuesto
                pass

        self.miembros: List[Usuario] = []

        for miembro_id in familia.listaMiembros:
            for user in listaUsuarios:
                if user.id == miembro_id:
                    self.miembros.append(user)
                    self.presupuesto_total += user.presupuesto

        self.planes_ahorro = [{'meta': plan.meta, 'duracion': plan.duracion, 'frecuencia': plan.frecuencia} for plan in familia.listaPlanDeAhorro]
        self.gastos_por_categoria = self.calcular_gastos_por_categoria(familia)
        self.estadisticas_gastos = self.calcular_estadisticas_gastos(familia)

    def calcular_gastos_por_categoria(self, familia: Familia):
        gastos_por_categoria = defaultdict(float)
        for miembro in self.miembros:
            for gasto in miembro.listaGastos:
                gastos_por_categoria[gasto.categoria] += gasto.monto()
        return dict(gastos_por_categoria)

    def calcular_estadisticas_gastos(self, familia):
        gastos_totales = sum(gasto.monto() for miembro in self.miembros for gasto in miembro.listaGastos)
        promedio_gastos_mensuales = gastos_totales / 12  # Asumiendo que los gastos son anuales

        gastos_por_categoria = self.calcular_gastos_por_categoria(familia)
        promedio_gastos_por_categoria = {categoria: monto / 12 for categoria, monto in gastos_por_categoria.items()}

        gastos_maximos_por_categoria = {}
        gastos_minimos_por_categoria = {}

        for categoria in gastos_por_categoria.keys():
            gastos_categoria = [gasto.monto() for miembro in self.miembros for gasto in miembro.listaGastos if gasto.categoria == categoria]
            if gastos_categoria:
                gastos_maximos_por_categoria[categoria] = max(gastos_categoria)
                gastos_minimos_por_categoria[categoria] = min(gastos_categoria)

        return {
            'promedio_gastos_mensuales': promedio_gastos_mensuales,
            'promedio_gastos_por_categoria': promedio_gastos_por_categoria,
            'gastos_maximos_por_categoria': gastos_maximos_por_categoria,
            'gastos_minimos_por_categoria': gastos_minimos_por_categoria
        }

    def generar_json(self):
        return {
            'fecha_reporte': datetime.now(),
            'id_familia': self.id_familia,
            'nombre_familia': self.nombre_familia,
            'presupuesto_total': self.presupuesto_total,
            'cabeza_familia': self.cabeza_familia,
            'miembros': self.miembros,
            'planes_ahorro': self.planes_ahorro,
            'gastos_por_categoria': self.gastos_por_categoria,
            'estadisticas_gastos': self.estadisticas_gastos,
        }