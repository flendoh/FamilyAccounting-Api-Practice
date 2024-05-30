from fastapi import FastAPI
from default_data import *

app = FastAPI()
app.title = "FamilyAccounting API"
app.version = "1.0.0"

ListaUsuarios = [user1, user2, user3, user4, user5, user6, user7, user8]
ListaFamilias = [familia1, familia2]

#USUARIO
@app.get("/usuario", tags=["Usuario"])
def mostrar_lista_usuarios():
    return ListaUsuarios

@app.get("/usuario/{user_id}", tags=["Usuario"])
def buscar_usuario_por_id(user_id: int):
    for i in ListaUsuarios:
        if i.id == user_id:
            return i
    return {"detail": "Usuario no encontrado"}

@app.post("/usuario", tags=["Usuario"])
def agregar_usuario(user: Usuario):
    for i in ListaUsuarios:
        if user.id == i.id:
            return {"detail": f"Ya existe un usuario con la misma Id"}
    ListaUsuarios.append(user)
    return {"detail": f"Se agrego el usuario: {user.nombre}"}           

@app.post("/usuario/{user_id}/addGasto", tags=["Usuario"])
def agregar_gasto_a_usuario(user_id: int, gasto: Gasto):
    for i in ListaUsuarios:
        if i.id == user_id:
            i.addGasto(gasto)
            return {"detail": "Gasto añadido"}
    return {"detail": "Usuario no encontrado"}
    
#FAMILIA
@app.get("/familia", tags=["Familia"])
def mostrar_lista_familias():
    return ListaFamilias

@app.get("/familia/{familia_id}", tags=["Familia"])
def buscar_familia_por_id(familia_id: int):
    for i in ListaFamilias:
        if i.id == familia_id:
            return i
    return {"detail": "Familia no encontrada"}

@app.post("/familia", tags=["Familia"])
def agregar_familia(familia: Familia, cabezaFamilia_id: int):
    ListaFamilias.append(familia)
    familia.cabezaFamilia = cabezaFamilia_id
    return {"detail": f"Se agrego la familia: {familia.id}"}

@app.post("/familia/{familia_id}/addMiembro", tags=["Familia"])
def agregar_miembro_a_familia(familia_id: int, user_id: int):
    for i in ListaFamilias:
        if i.id == familia_id:
            i.addMiembro(user_id)
            return {"detail": "Usuario añadido"}
    return {"detail": "Familia no encontrada"}

@app.post("/familia/{familia_id}/addPlanDeAhorro", tags=["Familia"])
def agregar_plan_de_ahorro_a_familia(familia_id: int, plan: PlanDeAhorro):
    for i in ListaFamilias:
        if i.id == familia_id:
            i.addPlanDeAhorro(plan)
            return {"detail": "Plan de ahorro añadido"}
    return {"detail": "Familia no encontrada"}