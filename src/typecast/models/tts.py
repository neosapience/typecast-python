from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class TTSModel(str, Enum):
    SSFM_V10 = "ssfm-v10"
    SSFM_V12 = "ssfm-v12"
    SSFM_V20 = "ssfm-v20"
    SSFM_V21 = "ssfm-v21"


class Prompt(BaseModel):
    emotion_preset: Optional[str] = Field(
        default="normal",
        description="Emotion preset",
        examples=["normal", "happy", "sad", "angry"],
    )
    emotion_intensity: Optional[float] = Field(default=1.0, ge=0.0, le=2.0)


class Output(BaseModel):
    volume: Optional[int] = Field(default=100, ge=0, le=200)
    audio_pitch: Optional[int] = Field(default=0, ge=-12, le=12)
    audio_tempo: Optional[float] = Field(default=1.0, ge=0.5, le=2.0)
    audio_format: Optional[str] = Field(
        default="wav", description="Audio format", examples=["wav", "mp3"]
    )


class TTSRequest(BaseModel):
    voice_id: str = Field(description="Voice ID", examples=["67b5c03d9cf5c7788b5a4a32"])
    text: str = Field(description="Text", examples=["Hello. How are you?"])
    model: TTSModel = Field(description="Voice model name", examples=["ssfm-v20"])
    language: Optional[str] = Field(None, description="Language", examples=["eng"])
    prompt: Optional[Prompt] = None
    output: Optional[Output] = None
    seed: Optional[int] = None

    class Config:
        json_schema_extra = {"exclude_none": True}


class TTSResponse(BaseModel):
    audio_data: bytes
    duration: float
    format: str = "wav"
