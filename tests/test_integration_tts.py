import os

import pytest

from typecast.client import Typecast
from typecast.models import TTSRequest, TTSResponse, VoicesResponse


@pytest.fixture
def typecast_client():
    # 환경 변수에서 API 키를 가져옵니다
    return Typecast()

class TestTypeCastIntegration:
    def test_text_to_speech_integration(self, typecast_client):
        # Arrange
        # 먼저 사용 가능한 voice를 가져옵니다
        voices = typecast_client.voices(model='ssfm-v21')
        voice = voices[0]
        
        voice_id = voice.voice_id
        model = voice.model
        
        request = TTSRequest(
            text="안녕하세요, 타입캐스트 테스트입니다.",
            voice_id=voice_id,
            model=model
        )

        # Act
        response = typecast_client.text_to_speech(request)

        # Assert
        assert isinstance(response, TTSResponse)
        assert response.audio_data is not None
        assert len(response.audio_data) > 0
        # assert float(response.duration) > 0
        assert response.format in ['wav', 'mp3']
