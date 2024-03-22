# typecast-python

## Basic example

```python
from typecast import Typecast

cli = Typecast(api_token='your token here!!')
audio = cli.generate_speech('A fence cuts through the corner lot.')

with open('out.wav', 'wb') as f:
    f.write(audio)
```

### Specify output format: mp3

```python
from typecast import Typecast

cli = Typecast(api_token='your token here!!')
audio = cli.generate_speech('A fence cuts through the corner lot.', filetype='mp3')

with open('out.mp3', 'wb') as f:
    f.write(audio)
```

## More documentations
* [API Documentation](https://docs.typecast.ai)
* [More demo](https://github.com/neosapience/typecast-api-demo)

