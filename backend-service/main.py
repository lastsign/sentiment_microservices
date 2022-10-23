from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import requests

def compute_sentiment(text="I liked this quick tutorial"):
    api_url = "http://model-torchserve-service:8080/predictions/sentiments"
    response = requests.post(api_url, data=text.encode('utf-8'), headers={'Content-Type': 'text/plain'})

    if response.status_code == 200: 
        predictionOut = str(response.content.decode())
        return predictionOut
    else:
        return "Bad request"

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")

templates = Jinja2Templates(directory="templates")

@app.post("/", response_class=HTMLResponse)
async def read_item(request: Request):
    form = await request.form()
    text = form["query"]
    if len(text) >= 1 and len(text) <= 2000:
        sentiment = compute_sentiment(text)
        return templates.TemplateResponse("homepage.html", {"request": request, "Sentiment": "Sentiment", "text": sentiment})
    else:
        return templates.TemplateResponse("homepage.html", {"request": request, "Sentiment": "Error", "text": "Bad request"})

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})
