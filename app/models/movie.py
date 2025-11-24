from pydantic import BaseModel

class MovieCreate(BaseModel):
    film: str
    genre: str
    lead_studio: str
    audience_score: int
    profitability: float
    rotten_tomatoes: int
    worldwide_gross: float
    year: int

class MovieUpdate(MovieCreate):
    pass
