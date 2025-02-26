import time

from typecast.client import Typecast
from typecast.models import TTSRequest
from typecast.utils import show_performance

# 클라이언트 초기화
cli = Typecast()

# 텍스트를 음성으로 변환
start_ts = time.time()
res = cli.text_to_speech(TTSRequest(
    text="Hello there! I'm your friendly text-to-speech agent. I can help you convert any text into natural sounding speech. I support multiple languages and voices, and I can even adjust the speed, pitch and volume of the generated audio. Would you like to try it out?",
    model="ssfm-v21",
    voice_id="67ae94ead6403a3574789fb2"
))
duration = time.time() - start_ts

# 오디오 파일로 저장
with open('typecast.wav', 'wb') as f:
    f.write(res.audio_data)

show_performance(duration, 'typecast.wav')
