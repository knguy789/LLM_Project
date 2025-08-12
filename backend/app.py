from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

# create FastAPI app
app = FastAPI()

# request body schema
class ChatRequest(BaseModel):
    prompt: str

# endpoint: POST /chat
@app.post("/chat")
def chat(req: ChatRequest):
    # send prompt to local Ollama server
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={"model":"llama3","prompt": req.prompt}
        )
        # parse JSON response body from ollama into python dict data
        data = res.json()
        # return JSON object to frontend using key "response"
        return {"response": data.get("response", "")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))