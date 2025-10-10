import os

import pytest

from typecast.client import Typecast
from typecast.exceptions import TypecastError
from typecast.models import TTSRequest, TTSResponse, VoicesResponse


@pytest.fixture
def typecast_client():
    # 환경 변수에서 API 키를 가져옵니다
    return Typecast()


@pytest.mark.skipif(
    not os.getenv("TYPECAST_API_KEY"), reason="TYPECAST_API_KEY not set"
)
class TestVoicesIntegration:
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

    def test_voices_with_model_filter_integration(self, typecast_client):
        target_model = 'ssfm-v21'

        # Act
        voices = typecast_client.voices(model=target_model)

        # Assert
        assert isinstance(voices, list)
        assert len(voices) > 0
        
        # 모든 voice가 지정된 model을 가지고 있는지 확인
        for voice in voices:
            assert voice.model == target_model
            assert voice.voice_id
            assert voice.voice_name
            assert voice.emotions

    def test_voices_with_invalid_model(self, typecast_client):
        target_model = 'non-existent-model'

        # Act
        with pytest.raises(TypecastError):
            typecast_client.voices(model=target_model)

    def test_get_voice_by_id(self, typecast_client):
        # Arrange - Get a voice first
        voices = typecast_client.voices()
        assert len(voices) > 0
        voice_id = voices[0].voice_id

        # Act
        voice = typecast_client.get_voice(voice_id)

        # Assert
        assert isinstance(voice, VoicesResponse)
        assert voice.voice_id == voice_id
        assert voice.voice_name
        assert voice.model
        assert voice.emotions
