import certifi
from pymongo import MongoClient

ca = certifi.where()

conn = MongoClient("mongodb+srv://brcanuto:j0N0QLM5aKR2JPOQ@filmsanddo.kaxeh.mongodb.net/?retryWrites=true&w=majority&appName=Filmsanddo", tlsCAFile=ca)
db = conn.filmes