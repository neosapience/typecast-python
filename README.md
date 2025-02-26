# Typecast SDK

Python SDK for Typecast API integration. For comprehensive API documentation and usage guidelines, please visit our [official documentation](https://neosapienceinc.mintlify.app/overview).

## Installation

```bash
pip install typecast-sdk
```

## Quick Start

```python
from typecast.client import Typecast
from typecast.models import TTSRequest

# Initialize client
cli = Typecast(api_key="YOUR_API_KEY")

# Convert text to speech
audio = cli.text_to_speech(TTSRequest(
    text="Hello there! I'm your friendly text-to-speech agent.",
    model="ssfm-v21",
    voice_id="tc_123456789"
))

# Save audio file
with open('typecast.wav', 'wb') as f:
    f.write(audio)
```
## License

MIT License