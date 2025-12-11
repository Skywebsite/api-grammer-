# AI Writing Assistant API

A powerful AI-powered writing assistant API built with FastAPI and HuggingFace models. Provides grammar correction, text rewriting, summarization, and more.

## Features

✔ Spelling correction  
✔ Grammar correction  
✔ Sentence rewriting  
✔ Formal writing mode  
✔ Short/long rewrite  
✔ Summarization  
✔ Proofreading with explanations  

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
uvicorn main:app --reload
```

API will be available at: `http://127.0.0.1:8000/ai`

API Documentation: `http://127.0.0.1:8000/docs`

## 📮 API Usage

### Endpoint

**POST** `/ai`

### Request Body

```json
{
  "text": "your text here",
  "mode": "correct"
}
```

### Available Modes

- `correct` - Correct spelling and grammar
- `rewrite` - Rewrite sentence better
- `formal` - Rewrite in formal tone
- `casual` - Rewrite in casual tone
- `long` - Expand the text
- `short` - Summarize shortly
- `summary` - Create a summary
- `explain` - Proofread and explain mistakes

### Response Format

```json
{
  "mode": "correct",
  "original": "original text",
  "output": "corrected/processed text"
}
```

## 📝 Example Request

```bash
curl -X POST "http://127.0.0.1:8000/ai" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "i want too lern how to bild beter ai apis",
    "mode": "correct"
  }'
```

## 🧠 Model Information

Uses the **pszemraj/flan-t5-large-grammar-synthesis** model from HuggingFace.

## 🛠️ Tech Stack

- **FastAPI** - Modern web framework
- **HuggingFace Transformers** - NLP models
- **PyTorch** - Deep learning framework

## 📦 Requirements

- Python 3.7+
- See `requirements.txt` for dependencies

## 🌐 Deployment

This API can be deployed on Render, Heroku, or any platform that supports Python applications.

## 📄 License

MIT
