def serializeDict(item) -> dict:
    return {
        "id":str(item["_id"]),
        "title":item["title"],
        "poster":item["poster"],
        "overview":item["overview"],
        "runtime":item["runtime"],
        "voteAverage":item["voteAverage"],
        "link":item["link"]
    }
    
def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'}, 
            **{i:a[i] for i in a if i!='_id'}}
    
def serializeList(entity) -> list:
    return[serializeDict(a) for a in entity]    