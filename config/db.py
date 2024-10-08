import certifi
from pymongo import MongoClient

ca = certifi.where()

conn = MongoClient("mongodb+srv://1532:WdZgzxFCpbCoQ8yl@filmsanddo.kaxeh.mongodb.net/?retryWrites=true&w=majority&appName=Filmsanddo", tlsCAFile=ca)
db = conn.filmes
