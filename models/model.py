from pydantic import BaseModel

class Films(BaseModel):
    imdbid: str
    titulo: str
    sinopse: str
    duracao: str
    lancamento: str
    genero: str
    diretor: str
    atores: str
    renda: str
    nota: str
    metacritic: str
    rottentomatoes: str
    poster: str
    banner: str
    link: str
    legenda: str