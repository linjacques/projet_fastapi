from fastapi import FastAPI
from src.utils.db_con import Base, engine, SessionLocal
from src.utils.cleaning import import_movies_from_csv
from src.router.movie import router as movie_router
from src.models.db.schema import Movie

app = FastAPI(title="Movie API TP3")

# 1. Créer tables
Base.metadata.create_all(bind=engine)

# 2. Import CSV automatique si la table est vide
db = SessionLocal()
if db.query(Movie).first() is None:
    import_movies_from_csv(db)
db.close()

# 3. Routes
app.include_router(movie_router)
