import time

from fastapi import FastAPI, Request
from routers import races  # , drivers
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.perf_counter()
#     response = await call_next(request)
#     process_time = time.perf_counter() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     print(request.session)
#     return response

middleware = [Middleware(SessionMiddleware, secret_key="abcdew", path="/")]
# app.add_middleware(middleware[0])

app.add_middleware(SessionMiddleware, secret_key="clave_secreta_segura", path="/")


app.include_router(races.router)
# app.include_router(drivers.router)

# @app.get("/")
# async def root():
#     return {"message": "¡Hola desde FastAPI!"}


@app.get("/set-session/")
async def set_session(request: Request):
    request.session["llave"] = "valor"
    return {"mensaje": "Sesión establecida"}


@app.get("/get-session/")
async def get_session(request: Request):
    valor = request.session.get("llave")
    return {"valor": valor}


@app.get("/delete-session/", include_in_schema=False)
async def delete_session(request: Request):
    request.session.pop("llave", None)
    return {"mensaje": "Sesión eliminada"}
