def serializeDict(item) -> dict:
    return {
        "id":str(item["_id"]),
        "imdbid":item["imdbid"],
        "titulo":item["titulo"],
        "sinopse":item["sinopse"],
        "lancamento":item["lancamento"],
        "genero":item["genero"],
        "renda":item["renda"],
        "nota":item["nota"],
        "metacritic":item["metacritic"],
        "rottentomatoes":item["rottentomatoes"],
        "poster":item["poster"],
        "link":item["link"],
        "legenda":item["legenda"]
    }
    
def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'}, 
            **{i:a[i] for i in a if i!='_id'}}
    
def serializeList(entity) -> list:
    return[serializeDict(a) for a in entity]    