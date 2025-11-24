from sqlalchemy.orm import Session
from src.models.db.schema import Movie

def get_movies(db: Session):
    return db.query(Movie).all()

def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def create_movie(db: Session, movie_data):
    movie = Movie(**movie_data.dict())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def update_movie(db: Session, movie_id: int, movie_data):
    movie = get_movie(db, movie_id)
    if not movie:
        return None
    for key, value in movie_data.dict().items():
        setattr(movie, key, value)
    db.commit()
    db.refresh(movie)
    return movie

def delete_movie(db: Session, movie_id: int):
    movie = get_movie(db, movie_id)
    if not movie:
        return False
    db.delete(movie)
    db.commit()
    return True
