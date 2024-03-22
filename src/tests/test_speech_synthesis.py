from typecastai import Typecast
import os


def test_speech_synthesis():
    cli = Typecast(api_token=os.environ['typecast_token'])
    audio = cli.generate_speech('A fence cuts through the corner lot.')
    with open('out-test_speech_synthesis.wav', 'wb') as f:
        f.write(audio)


def test_speech_synthesis_mp3():
    cli = Typecast(api_token=os.environ['typecast_token'])
    audio = cli.generate_speech('A fence cuts through the corner lot.', filetype='mp3')
    with open('out-test_speech_synthesis.mp3', 'wb') as f:
        f.write(audio)
