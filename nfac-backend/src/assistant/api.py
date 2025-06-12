from typing import Annotated

from fastapi import APIRouter, Depends

from .schemas import PromptRequest
from .service import save_conversation, get_conversation, ask_gemini
from ..auth.models import User
from ..auth.service import get_current_user

router = APIRouter()

@router.post("/chat/")
async def chat_with_ai(request: PromptRequest, current_user: Annotated[User, Depends(get_current_user)]):
    user_message = request.prompt
    user_id = f"{current_user.id}"

    history = get_conversation(user_id)
    gemini_response = ask_gemini(user_message, history)

    save_conversation(user_id, {"role": "user", "content": user_message})
    save_conversation(user_id, {"role": "assistant", "content": gemini_response})

    return {"response": gemini_response}