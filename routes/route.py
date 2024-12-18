from fastapi import APIRouter, HTTPException, Query
from models.model import Films
from config.db import conn
from pymongo.collection import Collection
from pymongo import ASCENDING, DESCENDING
from schemas.schema import serializeDict, serializeList
from bson import ObjectId

user = APIRouter()  # Removed redoc_url

@user.head('/')
@user.get('/')
async def main():
    return {'msg': 'Hello World'}

@user.get('/found')
async def Encontrar_Todos_Filmes():
    return serializeList(conn.filmes.filmes.find())

@user.get('/release')
async def Filmes_Por_Data(ordem: str = Query("asc", regex="^(asc|desc)$")):
    try:
        ordem_sort = 1 if ordem == "asc" else -1
        filmes_collection: Collection = conn.filmes.filmes
        results = filmes_collection.find({"lancamento": {"$exists": True}}).sort("lancamento", ordem_sort)
        filmes = serializeList(results)
        return filmes if filmes else {"message": "Nenhum filme encontrado."}
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro ao buscar filmes por data de lançamento.")

@user.get('/search')
async def procurar_filme(titulo: str):
    filmes_collection: Collection = conn.filmes.filmes
    results = filmes_collection.find({"titulo": {"$regex": titulo, "$options": "i"}})  
    filmes = serializeList(results)
    return filmes if filmes else {"message": "Nenhum filme encontrado."}

@user.get('/genero/{genero}')
async def Categoria_Filme(genero: str):
    filmes_collection: Collection = conn.filmes.filmes
    results = filmes_collection.find({"genero": {"$regex": genero, "$options": "i"}})
    filmes = serializeList(results)
    return filmes if filmes else {"message": "Nenhum filme encontrado."}

@user.get('/{iid}')
async def Encontrar_Filme(iid: str):
    filme = conn.filmes.filmes.find_one({"_id": ObjectId(iid)})
    if filme:
        return serializeDict(filme)
    else:
        raise HTTPException(status_code=404, detail="Filme não encontrado")

@user.post('/receive-data')
async def Adicionar_Filme(user: Films):
    conn.filmes.filmes.insert_one(dict(user))
    return serializeList(conn.filmes.filmes.find())

@user.put('/{iid}')
async def Atualizar_Filme(iid: str, user: Films):
    result = conn.filmes.filmes.find_one_and_update(
        {"_id": ObjectId(iid)}, 
        {"$set": dict(user)},
        return_document=True
    )
    if result:
        return serializeDict(result)
    else:
        raise HTTPException(status_code=404, detail="Filme não encontrado")

@user.delete('/{iid}')
async def Deletar_Filme(iid: str):
    result = conn.filmes.filmes.find_one_and_delete({"_id": ObjectId(iid)})
    if result:
        return serializeDict(result)
    else:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
