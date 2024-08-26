from pymongo import MongoClient

conn = MongoClient("mongodb+srv://brcanuto:j0N0QLM5aKR2JPOQ@filmsanddo.kaxeh.mongodb.net/?retryWrites=true&w=majority&appName=Filmsanddo")
db = conn.filmes