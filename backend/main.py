from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateRequest(BaseModel):
    prompt: str


@app.post("/generate")
def generate(request: GenerateRequest):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"prompt": request.prompt, "stream": False, "model": "gemma3:1b"},
    )

    return Response(content=response.text, media_type="application/json")
