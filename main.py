from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AI Model - Using smaller model for Render free tier compatibility
# For local: use "pszemraj/flan-t5-large-grammar-synthesis" (better quality, needs more RAM)
# For Render free tier: use "pszemraj/flan-t5-base-grammar-synthesis" (smaller, fits 512MB)
model_name = "pszemraj/flan-t5-base-grammar-synthesis"  # Smaller model for production
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

class RequestModel(BaseModel):
    text: str
    mode: str = "correct"  
    # modes → correct | rewrite | formal | casual | long | short | summary | explain

def generate_ai_output(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=256)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.post("/ai")
async def ai_tool(req: RequestModel):
    text = req.text
    mode = req.mode.lower()

    if mode == "correct":
        prompt = f"grammar: {text}"

    elif mode == "rewrite":
        prompt = f"rewrite: {text}"

    elif mode == "formal":
        prompt = f"rewrite formally: {text}"

    elif mode == "casual":
        prompt = f"rewrite casually: {text}"

    elif mode == "long":
        prompt = f"expand this text: {text}"

    elif mode == "short":
        prompt = f"summarize shortly: {text}"

    elif mode == "summary":
        prompt = f"summarize: {text}"

    elif mode == "explain":
        prompt = f"proofread and explain mistakes: {text}"

    else:
        return {"error": "Invalid mode. Use correct | rewrite | formal | casual | long | short | summary | explain"}

    result = generate_ai_output(prompt)

    return {
        "mode": mode,
        "original": text,
        "output": result
    }

