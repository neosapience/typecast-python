from typing import Optional

from pydantic import BaseModel


class TTSRequest(BaseModel):
    text: str
    model: str
    character_id: str
    speed: Optional[float] = None
    pitch: Optional[float] = None
    volume: Optional[float] = None

    class Config:
        json_schema_extra = {"exclude_none": True}


class TTSResponse(BaseModel):
    audio_data: bytes
    duration: float
    format: str = "wav"


class WebSocketMessage(BaseModel):
    type: str
    payload: dict


class Error(BaseModel):
    code: str
    message: str
    details: Optional[dict] = None
