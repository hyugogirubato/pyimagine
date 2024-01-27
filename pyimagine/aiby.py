import re
import time
from datetime import datetime

import requests
from requests import Response
from requests_toolbelt import MultipartEncoder

from pyimagine.constants import Ratio, Style, NSFW_NEGATIVE, NSFW
from pyimagine.utils import purify


class Arta:

    def __init__(self, restricted: bool = True, timeout: int = 120):
        self.secure_token = 'https://securetoken.googleapis.com/v1/token'
        self.identity_toolkit = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty'
        self.aiby = 'https://aiby.mobi/ai_art_android'
        self.dream = 'https://dream-api.aiby.mobi'

        self.restricted = restricted
        self.timeout = timeout
        self.account = {}

    def __request(self, **kwargs) -> Response:
        headers = {
            'Accept': '*/*',
            'User-Agent': 'AiArt/2.21.6 okHttp/4.10.0 Android UPSIDE_DOWN_CAKE',
            **kwargs.get('headers', {})
        }

        r = requests.request(
            method=kwargs.get('method', 'GET'),
            url=kwargs.get('url'),
            params=kwargs.get('params'),
            data=kwargs.get('data'),
            json=kwargs.get('json'),
            headers=headers,
            timeout=self.timeout
        )
        try:
            r.raise_for_status()
        except Exception as e:
            raise Exception(r.text)
        return r

    def __token(self) -> str:
        if not self.account:
            self.signupNewUser()
        elif self.account['expiresIn'] < time.time():
            data = self.__request(
                method='POST',
                url=self.secure_token,
                params={'key': self.account['key']},
                json={
                    'grantType': 'refresh_token',
                    'refreshToken': self.account['refreshToken']
                },
                headers={
                    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; Mi A2 Build/QKQ1.190910.002)',
                    'X-Android-Cert': '61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81',
                    'X-Android-Package': 'ai.generated.art.maker.image.picture.photo.generator.painting',
                    'X-Client-Version': 'Android/Fallback/X21001000/FirebaseCore-Android',
                    'X-Firebase-Client': 'H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA',
                    'X-Firebase-GMPID': '1:713239656559:android:f9e37753e9ee7324cb759a'
                }
            ).json()

            self.account = {
                'expiresIn': time.time() + int(data['expires_in']),
                'idToken': data['id_token'],
                'refreshToken': data['refresh_token']
            }

        return self.account['idToken']

    def signupNewUser(self) -> dict:
        key = 'AIzaSyB3-71wG0fIt0shj0ee4fvx1shcjJHGrrQ'
        data = self.__request(
            method='POST',
            url=f'{self.identity_toolkit}/signupNewUser',
            params={'key': key},
            json={},
            headers={
                'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 14; sdk_gphone64_x86_64 Build/UE1A.230829.036.A1)',
                'X-Android-Cert': '61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81',
                'X-Android-Package': 'ai.generated.art.maker.image.picture.photo.generator.painting',
                'X-Client-Version': 'Android/Fallback/X21001000/FirebaseCore-Android',
                'X-Firebase-Client': 'H4sIAAAAAAAAAFVS0Y6CMBD8FdJnW6By6PkrhzErXbCxtKSshovx369CQe-x05np7Gwf7ILg6YxAAzv8PBi0aIkdmMK7rpFb6LBKB3U9tf3FWSyL07gvT2WRNNojr81QpflebMVXBJwPfJkFJE-ujoy2gSD2QuYJWOWdVlzbgcAY9FU6i5q6C5qgEHIGwIL5JV0HcxlAkb3N-ZXG9YGZfKPLxMsXHpzpP1A3bdS93N5JegPUON8tQciDHXrnaRoqF7sk1tA5haZKsbuVxQirnsC3SDzUU6XbWEmPvlkDLsRO25klv9fi5kSf5UX25BUfPodEAWidaw2ubcVhPhqLnQJpZ18r2YWr7Xzl63Xu6azMUg7bMAWEr8UzmcmCZzmXJTs-jxt2Rz8Er_ATJHv-ATxj1gUmAgAA',
                'X-Firebase-GMPID': '1:713239656559:android:f9e37753e9ee7324cb759a'
            }
        ).json()

        data.update({
            'expiresIn': time.time() + int(data['expiresIn']),
            'key': key
        })
        self.account = data
        return data

    def getAccountInfo(self) -> dict:
        return self.__request(
            method='POST',
            url=f'{self.identity_toolkit}/getAccountInfo',
            params={'key': self.account.get('key')},
            json={'idToken': self.__token()},
            headers={
                'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 14; sdk_gphone64_x86_64 Build/UE1A.230829.036.A1)',
                'X-Android-Cert': '61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81',
                'X-Android-Package': 'ai.generated.art.maker.image.picture.photo.generator.painting',
                'X-Client-Version': 'Android/Fallback/X21001000/FirebaseCore-Android',
                'X-Firebase-Client': 'H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA',
                'X-Firebase-GMPID': '1:713239656559:android:f9e37753e9ee7324cb759a'
            }
        ).json()

    def selfie_info(self, selfie_id: str = None, popular: bool = True) -> dict:
        path = 'content/release/selfie_styles'
        if popular: path = f'{path}/popular'
        if selfie_id: path = f'{path}/{selfie_id}'
        return self.__request(method='GET', url=f'{self.aiby}/{path}/info.json').json()

    def selfie_preview(self, preview: str, selfie_id: str = None, popular: bool = True) -> bytes:
        path = 'content/release/selfie_styles'
        if popular: path = f'{path}/popular'
        if selfie_id: path = f'{path}/{selfie_id}'
        return self.__request(method='GET', url=f'{self.aiby}/{path}/{preview}').content

    def styles_info(self, style_id: str = None, popular: bool = False) -> dict:
        path = 'content/release/styles_v5'
        if popular: path = f'{path}/popular'
        if style_id: path = f'{path}/{style_id}'
        return self.__request(method='GET', url=f'{self.aiby}/{path}/info.json').json()

    def styles_preview(self, preview: str, style_id: str = None, popular: bool = False) -> bytes:
        path = 'content/release/styles_v5'
        if popular: path = f'{path}/popular'
        if style_id: path = f'{path}/{style_id}'
        return self.__request(method='GET', url=f'{self.aiby}/{path}/{preview}').content

    def banners_config(self) -> dict:
        return self.__request(method='GET', url=f'{self.aiby}/conf/release/banners/v1/config.json').json()

    def inspired(self, to_date: datetime = datetime.now(), limit: int = 50, page: int = 1) -> dict:
        return self.__request(
            method='GET',
            url=f'{self.dream}/api/v1/inspired',
            params={
                'to_date': to_date.strftime('%Y-%m-%d %H:%M:%S'),
                'limit': limit,
                'page': page
            },
            headers={'Authorization': self.__token()}
        ).json()

    def __analyse(self, prompt: str, negative: bool = False) -> str:
        prompt = prompt.strip().lower().split(' ')
        for i, word in enumerate(prompt):
            word = re.sub(r'[^a-zA-Z]', '', word)
            if (word in NSFW_NEGATIVE) if negative else (word in NSFW):
                if self.restricted:
                    raise Exception(f'Banned word found: {word}')
                else:
                    prompt[i] = prompt[i].replace(word, purify(word))

        return ' '.join(prompt)

    def infer(
            self,
            prompt: str,
            negative_prompt: str = None,
            style: Style = Style.REALISTIC_2,
            aspect_ratio: Ratio = Ratio.R1X1,
            images_num: int = 1,
            steps: int = 30,
            image_upscale: bool = True,
            cfg_scale: int = 7
    ) -> [str]:
        assert 1 <= cfg_scale <= 20, 'Invalid CFG Scale'
        assert 10 <= steps <= 50, 'Invalid Steps'

        mp_encoder = MultipartEncoder(fields={
            'prompt': self.__analyse(prompt, negative=False),
            'negative_prompt': self.__analyse(negative_prompt or '', negative=True),
            'style': style.value,
            'output_format': 'url',
            'aspect_ratio': aspect_ratio.value,
            'images_num': str(images_num),
            'steps': str(steps),
            'image_upscale': 'true' if image_upscale else 'false',
            'cfg_scale': str(cfg_scale)
        })

        data = self.__request(
            method='POST',
            url=f'{self.dream}/v2/models/ai_generated_art/versions/2/infer',
            data=mp_encoder,
            headers={
                'Content-Type': mp_encoder.content_type,
                'Authorization': self.__token()
            }
        ).json()
        urls = [f['url'] for f in data['files'] if not f['isBlur']]
        if not urls:
            raise Exception('Content has been banned')
        return urls

    def like(self, image_url: str) -> dict:
        return self.__request(
            method='POST',
            url=f'{self.dream}/api/v1/like',
            data={'image_url': image_url},
            headers={'Authorization': self.__token()}
        ).json()

    def image2text(self, content: bytes, language_code: str = 'en') -> str:
        mp_encoder = MultipartEncoder(fields={
            'image': ('@1.jpg', content, 'image/jpg'),
            'language_code': language_code
        })

        return self.__request(
            method='POST',
            url=f'{self.dream}/v2/models/ai_generated_art/image2text',
            data=mp_encoder,
            headers={
                'Content-Type': mp_encoder.content_type,
                'Authorization': self.__token()
            }
        ).json()['prompt']
