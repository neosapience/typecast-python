from . import actor
from .error import ApiError

import requests
import random
import time
# from io import BytesIO


class Typecast:
    def __init__(self, api_token) -> None:
        self._host = 'https://typecast.ai'
        self._headers = {
            'Authorization': f'Bearer {api_token}'
        }
        self._actors = actor.Actors()
    
    def generate_speech(self, text, actor=None, filetype='wav'):
        if not actor:
            actor = random.sample(self._actors.get_ssfm_sample_actors(), 1)[0]

        polling_url = self._request(text, actor, filetype)
        return self._polling(polling_url)

    def _request(self, text, actor, filetype):
        r = requests.post(f'{self._host}/api/speak', headers=self._headers, json={
            'text': text, 
            'actor_id': actor['actor_id'],
            'model_version': actor['model_version'],
            'xapi_hd': True,
            'lang': 'auto',
            'xapi_audio_format': filetype,
        })
        if r.status_code != 200:
            raise ApiError(r.status_code, r.content)

        return r.json()['result']['speak_v2_url']

    def _polling(self, url):
        for _ in range(120):
            r = requests.get(url, headers=self._headers)
            if r.status_code != 200:
                raise ApiError(r.status_code, r.content)
            
            ret = r.json()['result']
            if ret['status'] == 'done':
                # download audio file
                r = requests.get(ret['audio_download_url'])
                return r.content
            elif ret['status'] == 'failed':
                raise ApiError(r.status_code, 'polling error')
            else:
                print(f"status: {ret['status']}, waiting 1 second")
                time.sleep(1)
