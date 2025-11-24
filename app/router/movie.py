from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.utils.db_con import get_db
from src.services.movie import get_movies, get_movie, create_movie, update_movie, delete_movie
from src.models.movie import MovieCreate, MovieUpdate

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/")
def list_movies(db: Session = Depends(get_db)):
    return get_movies(db)


@router.get("/{movie_id}")
def get_one_movie(movie_id: int, db: Session = Depends(get_db)):
    mov_obj = get_movie(db, movie_id)
    if not mov_obj:
        raise HTTPException(status_code=404, detail="Film introuvable")
    return mov_obj


@router.post("/")
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db, movie)


@router.put("/{movie_id}")
def modify_movie(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):
    updated = update_movie(db, movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Film introuvable")
    return updated


@router.delete("/{movie_id}")
def delete(movie_id: int, db: Session = Depends(get_db)):
    deleted = delete_movie(db, movie_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Film introuvable")
    return {"message": "Film supprimé"}
