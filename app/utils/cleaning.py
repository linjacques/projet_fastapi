import csv
from sqlalchemy.orm import Session
from src.models.db.schema import Movie

def clean_money(value: str):
    value = value.replace("$", "").replace(",", "").strip()
    try:
        return float(value)
    except:
        return 0.0

def import_movies_from_csv(db: Session, path="/app/src/data/movies.csv"):
    try:
        with open("/app/src/data/movies.csv", encoding="utf8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                movie = Movie(
                    film=row["Film"],
                    genre=row["Genre"],
                    lead_studio=row["Lead Studio"],
                    audience_score=int(row["Audience score %"]),
                    profitability=float(row["Profitability"]),
                    rotten_tomatoes=int(row["Rotten Tomatoes %"]),
                    worldwide_gross=clean_money(row["Worldwide Gross"]),
                    year=int(row["Year"])
                )
                db.add(movie)
            db.commit()
    except FileNotFoundError:
        print("CSV introuvable, import ignoré.")
