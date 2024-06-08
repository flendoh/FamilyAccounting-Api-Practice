from model.Usuario import Usuario
from model.Gasto import Gasto
from model.Familia import Familia
from model.Reporte import Reporte
from model.PlanDeAhorro import PlanDeAhorro

# DATOS POR DEFECTO

# Usuarios
user1 = Usuario(id=0, nombre="Juan", presupuesto=50)
user2 = Usuario(id=1, nombre="Pedro", presupuesto=100)
user3 = Usuario(id=2, nombre="Maria", presupuesto=20)
user4 = Usuario(id=3, nombre="Carlos", presupuesto=60)
user5 = Usuario(id=4, nombre="Ana", presupuesto=20)
user6 = Usuario(id=5, nombre="Luis", presupuesto= 10)
user7 = Usuario(id=6, nombre="Sofia", presupuesto= 10)
user8 = Usuario(id=7, nombre="Diego", presupuesto=80)

# Gastos
gasto1 = Gasto(categoria="Comida", precio=100.0, cantidad=1)
gasto2 = Gasto(categoria="Renta", precio=500.0, cantidad=1)
gasto3 = Gasto(categoria="Transporte", precio=50.0, cantidad=1)
gasto4 = Gasto(categoria="Entretenimiento", precio=150.0, cantidad=2)
gasto5 = Gasto(categoria="Educación", precio=200.0, cantidad=1)
gasto6 = Gasto(categoria="Salud", precio=300.0, cantidad=1)
gasto7 = Gasto(categoria="Ropa", precio=75.0, cantidad=3)
gasto8 = Gasto(categoria="Utilidades", precio=120.0, cantidad=1)

# Asociar gastos a usuarios
user1.addGasto(gasto1)
user2.addGasto(gasto2)
user3.addGasto(gasto3)
user4.addGasto(gasto4)
user5.addGasto(gasto5)
user6.addGasto(gasto6)
user7.addGasto(gasto7)
user8.addGasto(gasto8)

# Familias
familia1 = Familia(id=0, nombreFamilia="Familia Gonzalez", listaMiembros=[user1.id, user2.id, user3.id, user4.id], cabezaFamilia=user4.id)
familia2 = Familia(id=1, nombreFamilia="Familia Perez", listaMiembros=[user5.id, user6.id, user7.id, user8.id], cabezaFamilia=user6.id)

