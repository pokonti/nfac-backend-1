import redis
import os
import json
from google import genai
from dotenv import load_dotenv

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True
)

def save_conversation(user_id: str, message: dict, ttl: int = 600):
    key = f"chat:{user_id}"
    messages = get_conversation(user_id)
    messages.append(message)
    redis_client.setex(key, ttl, json.dumps(messages))

def get_conversation(user_id: str) -> list:
    key = f"chat:{user_id}"
    data = redis_client.get(key)
    return json.loads(data) if data else []

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(message: str, history: list = None) -> str:
    try:
        messages = [{"role": m["role"], "parts": [m["content"]]} for m in (history or [])]
        messages.append({"role": "user", "parts": [message]})
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[f"{messages}"]
        )
        return response.text
    except Exception as e:
        return f"Gemini error: {str(e)}"