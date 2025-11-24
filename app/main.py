from fastapi import FastAPI
from src.router.book import router as book_router
from src.middleware.log import register_middleware
from src.handler.server_error import register_exception_handlers

app = FastAPI(title="Book API – TP")

register_middleware(app)

app.include_router(book_router)

register_exception_handlers(app)


@app.get("/")
def main_menu():
    return {"message": "TP2, jacques et thomas"}
