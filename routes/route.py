from fastapi import APIRouter
from models.model import Films
from config.db import conn
from schemas.schema import serializeDict, serializeList
from bson import ObjectId

user = APIRouter()

@user.head('/')
@user.get('/')
async def main():
    return {'msg': 'Hello World'}

@user.get('/found')
async def Encontrar_Todos_Filmes():
    return serializeList(conn.filmes.filmes.find())

@user.get('/{id}')
async def Encontrar_Filme(iid):
    return serializeDict(conn.filmes.filmes.find_one({"_id": ObjectId(iid)}))

@user.post('/receive-data')
async def Adicionar_Filme(user: Films):
    conn.filmes.filmes.insert_one(dict(user))
    return serializeList(conn.filmes.filmes.find())

@user.put('/{id}')
async def Atualizar_Filme(iid, user: Films):
    conn.filmes.filmes.find_one_and_update({"_id": ObjectId(iid)}, {
        "$set": dict(user)
    })
    return serializeDict(conn.filmes.filmes.find_one({"_id": ObjectId(iid)}))

@user.delete('/{id}')
async def Deletar_Filme(iid):
    return serializeDict(conn.filmes.filmes.find_one_and_delete({"_id": ObjectId(iid)}))