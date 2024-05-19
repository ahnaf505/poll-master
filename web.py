from fastapi import FastAPI
from auth import *
from database import *

app = FastAPI()

polls = [
    {"id": 1, "question": "What is your favorite color?", "options": ["Red", "Blue", "Green"]},
    {"id": 2, "question": "Which programming language do you prefer?", "options": ["Python", "JavaScript", "Java"]},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to Poll Master! Use /polls to view available polls."}

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
