from pydantic import BaseModel

class Films(BaseModel):
    imdbid: str
    titulo: str
    sinopse: str
    lancamento: str
    genero: str
    renda: str
    nota: str
    metacritic: str
    rottentomatoes: str
    poster: str
    link: str
    legenda: str