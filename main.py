from fastapi import FastAPI
from fastapi import FastAPI, HTTPException  # <-- Modifica tu import arriba

app = FastAPI(title="TechStore API")

# ------- BASE DE DATOS FALSA (en memoria) ------------
productos = [
    {"id" : 1 , "nombre" : "Laptop Pro", "categoria" : "computadoras", "precio": 1200, "stock":5},
    {"id" : 2 , "nombre" : "Mouse Inalámbrico", "categoria" : "accesorios", "precio": 25, "stock":50},
    {"id" : 3 , "nombre" : "Teclado Mecánico", "categoria" : "accesorios", "precio": 80, "stock":0},
    {"id" : 4 , "nombre" : "Monitor 27\"", "categoria" : "computadoras", "precio": 300, "stock":12},
    {"id" : 5 , "nombre" : "Audífonos BT", "categoria" : "audio", "precio": 60, "stock":30},
    {"id" : 6 , "nombre" : "Parlante Mini", "categoria" : "audio", "precio": 45, "stock":8},
    {"id" : 7 , "nombre" : "Tablet 10\"", "categoria" : "computadoras", "precio": 250, "stock":15}
]


# ------- ENDPOINT DE BIENVENIDA ---------
@app.get("/")
async def inicio():
    return {"mensaje": "Bienvenido a TechStore 🛒","total_productos": len(productos)}



# ---------- PATH PARAMETER: un producto específico ----------
@app.get("/productos/{producto_id}")
async def obtener_producto(producto_id: int):
    # LÓGICA REAL: buscar en la lista el producto con ese ID
    for producto in productos:
        if producto["id"] == producto_id:
            return producto

    # Si llegamos aquí, el producto NO existe → error 404
    raise HTTPException(
        status_code=404,
        detail=f"El producto con id {producto_id} no existe 🤷"
    )