from fastapi import FastAPI
from router.note import note
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/static", StaticFiles(directory="D:\python project\static"), name="static")

app.include_router(note)


