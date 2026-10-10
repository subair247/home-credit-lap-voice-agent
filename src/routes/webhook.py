from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from src.agent.system_prompt import get_system_prompt
from src.services.validation import validate_eligibility

router = APIRouter()

class WebhookRequest(BaseModel):
    customer_name: Optional[str] = "Valued Customer"
    language_to_speak: Optional[str] = "English"
    current_state: Optional[Dict[str, Any]] = {}
    customer_utterance: Optional[str] = ""

@router.post("/webhook")
async def voice_webhook(payload: WebhookRequest):
    try:
        prompt = get_system_prompt(customer_name=payload.customer_name, language_to_speak=payload.language_to_speak)
        validation_result = validate_eligibility(payload.current_state)
        
        return {
            "status": "success",
            "system_prompt": prompt,
            "validation_status": validation_result,
            "response_message": "Processed successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))