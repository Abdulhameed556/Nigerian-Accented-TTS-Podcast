from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class TTSRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000, description="Text to convert to speech")
    language: str = Field(default="english", description="Language for speech synthesis")
    voice: str = Field(default="idera", description="Voice to use for speech synthesis")
    
    class Config:
        schema_extra = {
            "example": {
                "text": "Hello, this is a test of the Nigerian TTS system.",
                "language": "english",
                "voice": "idera"
            }
        }

class TTSResponse(BaseModel):
    audio_base64: str = Field(..., description="Base64-encoded audio data")
    audio_url: str = Field(..., description="URL to access the audio file")
    text: str = Field(..., description="Original text that was synthesized")
    voice: str = Field(..., description="Voice used for synthesis")
    language: str = Field(..., description="Language used for synthesis")
    duration: Optional[float] = Field(None, description="Estimated duration in seconds")
    generated_at: datetime = Field(default_factory=datetime.now, description="Generation timestamp")

class HealthResponse(BaseModel):
    status: str = Field(..., description="Health status")
    model_loaded: bool = Field(..., description="Whether the TTS model is loaded")
    timestamp: str = Field(..., description="Current timestamp")
    version: str = Field(..., description="API version")
    uptime: Optional[float] = Field(None, description="Server uptime in seconds")

class VoicesResponse(BaseModel):
    female: List[str] = Field(..., description="Available female voices")
    male: List[str] = Field(..., description="Available male voices")

class LanguagesResponse(BaseModel):
    languages: List[str] = Field(..., description="Supported languages")

class APIInfoResponse(BaseModel):
    status: str
    message: str
    version: str
    available_languages: List[str]
    available_voices: Dict[str, List[str]]
    model_loaded: bool

class ErrorResponse(BaseModel):
    detail: str = Field(..., description="Error description")
    error_code: Optional[str] = Field(None, description="Error code")
    timestamp: datetime = Field(default_factory=datetime.now)