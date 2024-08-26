from pydantic import BaseModel

class Films(BaseModel):
    title: str
    poster: str
    overview: str
    runtime: str
    voteAverage: str
    link: str