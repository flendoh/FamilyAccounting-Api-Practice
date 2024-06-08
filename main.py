from fastapi import FastAPI
from default_data import *
from fastapi.responses import Response
from fastapi.responses import RedirectResponse

app = FastAPI()
app.title = "FamilyAccounting API"
app.version = "1.0.1"

ListaUsuarios = [user1, user2, user3, user4, user5, user6, user7, user8]
ListaFamilias = [familia1, familia2]
@app.get("/")
def root():
    return RedirectResponse("./docs")

#USUARIO
@app.get("/usuario", tags=["Usuario"])
def mostrar_lista_usuarios():
    return ListaUsuarios

@app.get("/usuario/{user_id}", tags=["Usuario"])
def buscar_usuario_por_id(user_id: int):
    for i in ListaUsuarios:
        if i.id == user_id:
            return i
    return Response("Usuario no encontrado", status_code=404)

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
    return Response("Usuario no encontrado", status_code=404)
    
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
    return {"detail": f"Se agrego la familia: {familia.nombreFamilia}"}

@app.post("/familia/{familia_id}/addMiembro", tags=["Familia"])
def agregar_miembro_a_familia(familia_id: int, user_id: int):
    for familia in ListaFamilias:
        if familia.id == familia_id:
            if user_id not in familia.listaMiembros:
                familia.addMiembro(user_id)
                return {"detail": "Usuario añadido"}
            return {"detail": "Este usuario ya esta dentro de la familia"}
    return Response("Familia no encontrada", status_code=404)

@app.post("/familia/{familia_id}/addPlanDeAhorro", tags=["Familia"])
def agregar_plan_de_ahorro_a_familia(familia_id: int, plan: PlanDeAhorro):
    for i in ListaFamilias:
        if i.id == familia_id:
            i.addPlanDeAhorro(plan)
            return {"detail": "Plan de ahorro añadido"}
    return Response("Familia no encontrada", status_code=404)

@app.delete("/familia/{familia_id}/removeMiembro", tags=["Familia"])
def eliminar_miembro_familia(familia_id: int, user_id: int):
    for familia in ListaFamilias:
        if familia.id == familia_id:
            # Verificar si el usuario está en la lista de IDs de usuarios de esa familia
            if user_id in familia.listaMiembros:
                familia.listaMiembros.remove(user_id)
                return {"detail": f"Se eliminio el usuario {user_id}"}
    return Response(status_code=404)

@app.post("/familia/reporte", tags=["Familia"])
def generar_reporte(familia_id: int):
    for familia in ListaFamilias:
        if familia.id == familia_id:
            nuevoReporte = Reporte(familia, ListaUsuarios)
            return nuevoReporte.generar_json()
    
    return Response(status_code=404)
    