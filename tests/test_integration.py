import os

import pytest

from typecast.client import Typecast
from typecast.models import TTSRequest, TTSResponse, VoicesResponse


@pytest.fixture
def typecast_client():
    # 환경 변수에서 API 키를 가져옵니다
    return Typecast()

class TestTypeCastIntegration:
    def test_voices_integration(self, typecast_client):
        # Act
        voices = typecast_client.voices()

        # Assert
        assert isinstance(voices, list)
        assert len(voices) > 0
        
        # 첫 번째 voice의 필수 필드 검증
        first_voice = voices[0]
        assert first_voice.voice_id
        assert first_voice.voice_name
        assert first_voice.model
        assert first_voice.emotions

    def test_text_to_speech_integration(self, typecast_client):
        # Arrange
        # 먼저 사용 가능한 voice를 가져옵니다
        voices = typecast_client.voices()
        voice = None
        for v in voices:
            if v.model == 'ssfm-v21':
                voice = v
        
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
