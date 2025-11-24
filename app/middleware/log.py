from fastapi import FastAPI, Request

def register_middleware(app: FastAPI):
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        print(f"{request.method} {request.url}")
        response = await call_next(request)
        print(f"⬅{response.status_code}")
        return response
