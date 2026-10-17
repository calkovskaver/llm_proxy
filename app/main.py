import httpx
from fastapi import FastAPI, Request
from config import config
from security.input import InputSecurity
from db.database import Database
from datetime import datetime, timezone

app = FastAPI(title="LLM Gateway")
client = httpx.AsyncClient()

@app.get("/")
async def root():
    return {"message": "Welcome to LLM proxy!"}

@app.post("/v1/chat/completions")
async def root(request:Request):
    req_body = await request.json()

    url = config.API_HOST

    headers = {k: v for k, v in request.headers.items() if
                k not in {'host', 'content-length', 'x-forwarded-for', 'x-real-ip', 'connection'}}
    data = req_body

    messages = data.get("messages", [])
    message_content = " ".join([msg.get("content", "") for msg in messages])

    inection_detected = InputSecurity.detect_injection(message_content)
    if inection_detected:
        return {"error": "Injection detected in the input."}, 403
    
    pii_detected = InputSecurity.detect_pii(message_content)
    if pii_detected:
        return {"error": "PII detected in the input."}, 403
    sensitive_info_detected = InputSecurity.detect_user_specific_sensitive_info(message_content)
    if sensitive_info_detected:
        return {"error": "User-specific sensitive information detected in the input."}, 403

    try:
        r = await client.post(url=url, headers=headers, json=data)
    except Exception as e:
        print(e)
        return {"error": e}, 403

    response = r.json()
    tokens = response['usage']['total_tokens']

    Database.insert_log("default_user", req_body["model"], tokens, datetime.now(timezone.utc).isoformat())
   

    return response