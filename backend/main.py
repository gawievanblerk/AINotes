from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# OAuth2 configuration
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://accounts.google.com/o/oauth2/auth",
    tokenUrl="https://oauth2.googleapis.com/token"
)

class Note(BaseModel):
    id: int
    title: str
    content: str
    tags: List[str] = []

notes = []

# Dependency to get the current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Here you would validate the token with Google and extract user information
    # For simplicity, we'll assume the token is valid and return a dummy user
    user = {"id": "123", "email": "user@example.com"}
    return user

@app.post("/notes/", response_model=Note)
async def create_note(note: Note, user: dict = Depends(get_current_user)):
    notes.append(note)
    return note

@app.get("/notes/", response_model=List[Note])
async def read_notes(user: dict = Depends(get_current_user)):
    return notes

@app.put("/notes/{note_id}", response_model=Note)
async def update_note(note_id: int, note: Note, user: dict = Depends(get_current_user)):
    for n in notes:
        if n.id == note_id:
            n.title = note.title
            n.content = note.content
            n.tags = note.tags
            return n
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int, user: dict = Depends(get_current_user)):
    global notes
    notes = [n for n in notes if n.id != note_id]
    return {"detail": "Note deleted"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
