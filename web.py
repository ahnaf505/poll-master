from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from auth import *
from database import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/polls")
def read_polls():
    return polls

@app.get("/polls/{poll_id}")
def read_poll(poll_id: int):
    for poll in polls:
        if poll["id"] == poll_id:
            return poll
    return {"error": "Poll not found"}

@app.post("/polls/{poll_id}/vote/{option}")
def vote(poll_id: int, option: str):
    for poll in polls:
        if poll["id"] == poll_id:
            if option in poll["options"]:
                return {"message": f"Voted for {option} in poll {poll_id}"}
            else:
                return {"error": f"{option} is not a valid option for poll {poll_id}"}
    return {"error": "Poll not found"}
