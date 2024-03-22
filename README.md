# typecastai-python
* [Typecast.ai](https://typecast.ai)
* [Get API Token](https://biz.typecast.ai)
* [Learn about Typecast SSFM(Speech Synthesis Foundation Model) v1](https://typecast.ai/learn/typecast-ssfm-text-to-speech/)

## Basic example

```python
from typecastai import Typecast

cli = Typecast(api_token='your token here!!')
audio = cli.generate_speech('A fence cuts through the corner lot.')

with open('out.wav', 'wb') as f:
    f.write(audio)
```

### Specify output format: mp3

```python
from typecastai import Typecast

cli = Typecast(api_token='your token here!!')
audio = cli.generate_speech('A fence cuts through the corner lot.', filetype='mp3')

with open('out.mp3', 'wb') as f:
    f.write(audio)
```

## More documentations
* [API Documentation](https://docs.typecast.ai)
* [More demo](https://github.com/neosapience/typecast-api-demo)

