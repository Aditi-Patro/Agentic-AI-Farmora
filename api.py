# You can use FastAPI or Streamlit. Here's a FastAPI starter.

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Sustainable Farming AI API"}
