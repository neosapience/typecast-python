from typing import Optional

import requests

from . import conf
from .exceptions import TypecastError
from .models import TTSRequest, TTSResponse, VoicesResponse


class Typecast:
    """Typecast API Client"""

    def __init__(self, host: Optional[str] = None, api_key: Optional[str] = None):
        self.host = conf.get_host(host)
        self.api_key = conf.get_api_key(api_key)
        self.session = requests.Session()
        self.session.headers.update(
            {"X-API-KEY": self.api_key, "Content-Type": "application/json"}
        )

    def text_to_speech(self, request: TTSRequest) -> TTSResponse:
        endpoint = "/v1/text-to-speech"
        response = self.session.post(
            f"{self.host}{endpoint}", json=request.model_dump(exclude_none=True)
        )
        if response.status_code != 200:
            raise TypecastError(
                f"API request failed: {response.status_code}, {response.text}"
            )

        return TTSResponse(
            audio_data=response.content,
            duration=response.headers.get("X-Audio-Duration", 0),
            format=response.headers.get("Content-Type", "audio/wav").split("/")[-1],
        )

    def voices(self, model: Optional[str] = None) -> list[VoicesResponse]:
        endpoint = "/v1/voices"
        params = {}
        if model:
            params["model"] = model

        response = self.session.get(f"{self.host}{endpoint}", params=params)

        if response.status_code != 200:
            raise TypecastError(
                f"API request failed: {response.status_code}, {response.text}"
            )

        return [VoicesResponse.model_validate(item) for item in response.json()]
