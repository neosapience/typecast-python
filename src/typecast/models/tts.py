from typing import Optional

from pydantic import BaseModel


class TTSRequest(BaseModel):
    text: str
    model: str
    voice_id: str
    speed: Optional[float] = None
    pitch: Optional[float] = None
    volume: Optional[float] = None
    language: Optional[str] = None

    class Config:
        json_schema_extra = {"exclude_none": True}


class TTSResponse(BaseModel):
    audio_data: bytes
    duration: float
    format: str = "wav"
