from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.post("/predict")
def predict(data: InputText):
    blob = TextBlob(data.text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    return {"sentiment": sentiment}