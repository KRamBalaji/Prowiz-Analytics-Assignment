import nest_asyncio
import uvicorn
from fastapi import FastAPI, Query

# Fix for running in Notebooks/Colab
nest_asyncio.apply()

app = FastAPI()

# --- NEW: Root Route ---
@app.get("/")
async def root():
    return {
        "message": "Welcome to my FastAPI Task!",
        "endpoints": {
            "sum": "/sum?num1=10&num2=20",
            "uppercase": "/uppercase?text=hello"
        },
        "docs": "/docs"
    }

# --- Task 3 (a): Sum with Validation ---
@app.get("/sum")
async def get_sum(num1: float, num2: float):
    # FastAPI automatically handles the "string instead of number" error here
    return {"num1": num1, "num2": num2, "sum": num1 + num2}

# --- Task 3 (b): Uppercase ---
@app.get("/uppercase")
async def to_uppercase(text: str):
    return {"original": text, "uppercase": text.upper()}

if __name__ == "__main__":
    # Running on port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)