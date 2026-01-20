# Typecast Python SDK

Python SDK for Typecast API integration. Convert text to lifelike speech using AI-powered voices with emotion, pitch, and tempo control.

For comprehensive API documentation, visit [Typecast Documentation](https://typecast.ai/docs/overview).

## Installation

```bash
pip install typecast-python
```

## Quick Start

```python
from typecast.client import Typecast
from typecast.models import TTSRequest

# Initialize client
cli = Typecast(api_key="YOUR_API_KEY")

# Convert text to speech
response = cli.text_to_speech(TTSRequest(
    text="Hello there! I'm your friendly text-to-speech agent.",
    model="ssfm-v21",
    voice_id="tc_62a8975e695ad26f7fb514d1"
))

# Save audio file
with open('output.wav', 'wb') as f:
    f.write(response.audio_data)

print(f"Duration: {response.duration}s, Format: {response.format}")
```

## Features

- 🎙️ **Multiple Voice Models**: Support for ssfm-v21 and ssfm-v30 AI voice models
- 🌍 **Multi-language Support**: 37 languages including English, Korean, Spanish, Japanese, Chinese, and more
- 😊 **Emotion Control**: Preset emotions (happy, sad, angry, whisper, toneup, tonedown) or smart context-aware inference
- 🎚️ **Audio Customization**: Control volume (0-200), pitch (-12 to +12 semitones), tempo (0.5x to 2.0x), and format (WAV/MP3)
- ⚡ **Async Support**: Built-in async client for high-performance applications
- 🔍 **Voice Discovery**: V2 API with filtering by model, gender, age, and use cases

## Advanced Usage

### Emotion and Audio Control

```python
from typecast.client import Typecast
from typecast.models import TTSRequest, Prompt, Output

cli = Typecast()

response = cli.text_to_speech(TTSRequest(
    text="I am so excited to show you these features!",
    model="ssfm-v21",
    voice_id="tc_62a8975e695ad26f7fb514d1",
    language="eng",
    prompt=Prompt(
        emotion_preset="happy",      # Options: normal, happy, sad, angry
        emotion_intensity=1.5        # Range: 0.0 to 2.0
    ),
    output=Output(
        volume=120,                  # Range: 0 to 200
        audio_pitch=2,               # Range: -12 to +12 semitones
        audio_tempo=1.2,             # Range: 0.5x to 2.0x
        audio_format="mp3"           # Options: wav, mp3
    ),
    seed=42                          # For reproducible results
))
```

### Voice Discovery

```python
from typecast.models import VoicesV2Filter, TTSModel, GenderEnum, AgeEnum

# V2 API (recommended) - Enhanced metadata with filtering
voices = cli.voices_v2()

# Filter by model, gender, age, or use case
filtered_voices = cli.voices_v2(VoicesV2Filter(
    model=TTSModel.SSFM_V30,
    gender=GenderEnum.FEMALE,
    age=AgeEnum.YOUNG_ADULT
))

# Each voice shows supported models and emotions
for voice in voices[:3]:
    print(f"Voice: {voice.voice_name}")
    print(f"Gender: {voice.gender}, Age: {voice.age}")
    print(f"Models: {', '.join(m.version.value for m in voice.models)}")

# V1 API (legacy)
v21_voices = cli.voices(model="ssfm-v21")
```

### Async Client

```python
import asyncio
from typecast.async_client import AsyncTypecast
from typecast.models import TTSRequest, LanguageCode

async def main():
    async with AsyncTypecast() as cli:
        response = await cli.text_to_speech(TTSRequest(
            text="Hello from async!",
            model="ssfm-v21",
            voice_id="tc_62a8975e695ad26f7fb514d1",
            language=LanguageCode.ENG
        ))
        
        with open('async_output.wav', 'wb') as f:
            f.write(response.audio_data)

asyncio.run(main())
```

### ssfm-v30 Model Features

The ssfm-v30 model offers enhanced emotion control with two modes:

#### Preset Emotion Control

```python
from typecast.models import TTSRequest, PresetPrompt, TTSModel

response = cli.text_to_speech(TTSRequest(
    text="I'm so happy to meet you!",
    voice_id="tc_672c5f5ce59fac2a48faeaee",
    model=TTSModel.SSFM_V30,
    language="eng",
    prompt=PresetPrompt(
        emotion_type="preset",
        emotion_preset="happy",      # normal, happy, sad, angry, whisper, toneup, tonedown
        emotion_intensity=1.5
    )
))
```

#### Smart Context-Aware Emotion

Let the AI infer emotion from surrounding context:

```python
from typecast.models import TTSRequest, SmartPrompt, TTSModel

response = cli.text_to_speech(TTSRequest(
    text="Everything is so incredibly perfect.",
    voice_id="tc_672c5f5ce59fac2a48faeaee",
    model=TTSModel.SSFM_V30,
    language="eng",
    prompt=SmartPrompt(
        emotion_type="smart",
        previous_text="I just got the best news ever!",
        next_text="I cannot wait to share this with everyone!"
    )
))
```

## Supported Languages

The SDK supports 37 languages with ISO 639-3 codes:

| Language | Code | Language | Code | Language | Code |
|----------|------|----------|------|----------|------|
| English | `eng` | Japanese | `jpn` | Ukrainian | `ukr` |
| Korean | `kor` | Greek | `ell` | Indonesian | `ind` |
| Spanish | `spa` | Tamil | `tam` | Danish | `dan` |
| German | `deu` | Tagalog | `tgl` | Swedish | `swe` |
| French | `fra` | Finnish | `fin` | Malay | `msa` |
| Italian | `ita` | Chinese | `zho` | Czech | `ces` |
| Polish | `pol` | Slovak | `slk` | Portuguese | `por` |
| Dutch | `nld` | Arabic | `ara` | Bulgarian | `bul` |
| Russian | `rus` | Croatian | `hrv` | Romanian | `ron` |
| Bengali | `ben` | Hindi | `hin` | Hungarian | `hun` |
| Hokkien | `nan` | Norwegian | `nor` | Punjabi | `pan` |
| Thai | `tha` | Turkish | `tur` | Vietnamese | `vie` |
| Cantonese | `yue` | | | | |

Use the `LanguageCode` enum for type-safe language selection:

```python
from typecast.models import LanguageCode

request = TTSRequest(
    text="Hello",
    language=LanguageCode.ENG,
    ...
)
```

## Error Handling

The SDK provides specific exceptions for different HTTP status codes:

```python
from typecast import (
    BadRequestError,           # 400
    UnauthorizedError,         # 401
    PaymentRequiredError,      # 402
    NotFoundError,             # 404
    UnprocessableEntityError,  # 422
    RateLimitError,            # 429
    InternalServerError,       # 500
    TypecastError              # Base exception
)

try:
    response = cli.text_to_speech(request)
except UnauthorizedError:
    print("Invalid API key")
except PaymentRequiredError:
    print("Insufficient credits")
except RateLimitError:
    print("Rate limit exceeded - please wait and retry")
except TypecastError as e:
    print(f"Error: {e.message}, Status: {e.status_code}")
```

## Examples

Check out the [examples](./examples) directory for more usage examples:

- [`simple.py`](./examples/simple.py) - Basic text-to-speech conversion
- [`advanced.py`](./examples/advanced.py) - Emotion, pitch, and tempo control
- [`voices_example.py`](./examples/voices_example.py) - Discovering available voices
- [`async_example.py`](./examples/async_example.py) - Async client usage

## Configuration

Set your API key via environment variable or constructor:

```bash
export TYPECAST_API_KEY="your-api-key-here"
```

```python
# From environment variable
cli = Typecast()

# Or pass directly
cli = Typecast(api_key="your-api-key-here")

# Custom host (optional)
cli = Typecast(host="https://custom-api.example.com")
```

## License

Apache License 2.0