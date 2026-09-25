import httpx
from fastapi import FastAPI, Request
from config import config

app = FastAPI(title="LLM Gateway")
client = httpx.AsyncClient()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/v1/chat/completions")
async def root(request:Request):
    req_body = await request.json()

    url = config.API_HOST

    headers = {k: v for k, v in request.headers.items() if
                k not in {'host', 'content-length', 'x-forwarded-for', 'x-real-ip', 'connection'}}
    data = req_body

    r = await client.post(url=url, headers=headers, json=data)
    response = r.json()
    tokens = response['usage']['total_tokens']
   

    return response