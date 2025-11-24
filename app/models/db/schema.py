from sqlalchemy import Column, Integer, String, Float
from src.utils.db_con import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    film = Column(String, nullable=False)
    genre = Column(String)
    lead_studio = Column(String)
    audience_score = Column(Integer)
    profitability = Column(Float)
    rotten_tomatoes = Column(Integer)
    worldwide_gross = Column(Float)
    year = Column(Integer)
