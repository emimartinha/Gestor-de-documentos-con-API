from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, Response
import database as db 
from pydantic import BaseModel, constr, field_validator
import helpers


class ModeloCliente(BaseModel):
    dni: constr(min_length=3,max_length=3)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2,max_length=30)

class ModeloCrearCliente(ModeloCliente):
    @field_validator("dni")
    @classmethod
    def validar_dni(cls, dni):
        if helpers.dni_valido(dni, db.Clientes.lista):
            return dni
        raise ValueError("Cliente ya existente")
        


app= FastAPI()

@app.get("/")
async def index():
    content= {"mensaje":"Hola mundo!"}
    return JSONResponse (content=content)

@app.get("/html/")
async def html():
    content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>¡Hola mundo!</title>
    </head>
    <body>
        <h1>¡Hola mundo!</h1>
    </body>
    </html>
    """
    return Response(content=content,media_type="text/html")

@app.get('/clientes/')
async def clientes():
    content= [
        {'dni':cliente.dni,'nombre':cliente.nombre,'apellido':cliente.apellido}
        for cliente in db.Clientes.lista
    ]    
    return JSONResponse(content=content)


@app.get("/clientes/buscar/{dni}")
async def clientes_buscar(dni:str):
    cliente = db.Clientes.buscar(dni=dni)
    return JSONResponse(content={'dni':cliente.dni,'nombre':cliente.nombre,'apellido':cliente.apellido})
print("Servidor de la API...")

@app.post('/clientes/crear/')
async def clientes_crear(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni,datos.nombre,datos.apellido)
    if cliente:
        return JSONResponse(content={'dni':cliente.dni,'nombre':cliente.nombre,'apellido':cliente.apellido})
    raise HTTPException(status_code=404)

@app.delete('clientes/borrar/{dni}/')
async def clientes_borrar(dni:str):
    if db.Clientes.buscar(dni):
        cliente = db.Clientes.borrar(dni=dni)
        return JSONResponse(content=[{'dni':cliente.dni,'nombre':cliente.nombre,'apellido':cliente.apellido}])
    raise HTTPException(status_code=404,detail="Cliente no encontrado")
