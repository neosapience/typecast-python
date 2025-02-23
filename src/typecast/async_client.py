from typing import Optional

import aiohttp

from . import conf
from .exceptions import TypecastError
from .models import Error, TTSRequest, TTSResponse


class AsyncTypecast:
    def __init__(self, host: Optional[str] = None, api_key: Optional[str] = None):
        self.host = conf.get_host(host)
        self.api_key = conf.get_api_key(api_key)
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            headers={"X-API-KEY": self.api_key, "Content-Type": "application/json"}
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def text_to_speech(self, request: TTSRequest) -> TTSResponse:
        if not self.session:
            raise TypecastError("Client session not initialized. Use async with.")
        endpoint = "/v1/text-to-speech/sse"
        async with self.session.post(
            f"{self.host}{endpoint}", json=request.model_dump()
        ) as response:
            if response.status != 200:
                error_data = await response.json()
                raise TypecastError(Error(**error_data))

            audio_data = await response.read()
            return TTSResponse(
                audio_data=audio_data,
                duration=float(response.headers.get("X-Audio-Duration", 0)),
                format=response.headers.get("Content-Type", "audio/wav").split("/")[-1],
            )
