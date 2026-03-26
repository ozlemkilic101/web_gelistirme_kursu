from fastapi import FastAPI,Request
from models import Base
from fastapi.staticfiles import StaticFiles
from database import engine
from routers.auth import router as auth_router
from routers.todo import router as todo_router
from starlette.responses import RedirectResponse
from starlette import status
app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/")
def read_root(request:Request):
    return RedirectResponse(url="/todo/todo-page",status_code=status.HTTP_302_FOUND)


app.include_router(auth_router)
app.include_router(todo_router)

Base.metadata.create_all(bind=engine)