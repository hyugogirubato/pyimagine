import re
from enum import Enum
from typing import Union

import requests
from langdetect import detect
from requests import Response
from requests_toolbelt import MultipartEncoder

from pyimagine.constants import Style, Inspiration, Ratio, Mode, BANNED_WORDS
from pyimagine.exceptions import InvalidWord
from pyimagine.utils import bytes2png, clear_dict, get_cfg, get_word


class DeviantArt(Enum):
    ID = 23185
    SECRET = "fae0145a0736611056a5196a122c0d36"


class Imagine:

    def __init__(self, restricted: bool = True):
        self.restricted = restricted
        self.api = "https://inferenceengine.vyro.ai"
        self.cdn = "https://1966211409.rsc.cdn77.org/appStuff/imagine-fncisndcubnsduigfuds"
        self.version = 1

    def _request(self, **kwargs) -> Response:
        headers = {"accept": "*/*", "user-agent": "okhttp/4.10.0"}
        headers.update(kwargs.get("headers", None) or {})

        data = clear_dict(kwargs.get("data"))
        if data:
            prompt = data.get("prompt", "").lower().split(" ")
            if prompt:
                for i, word in enumerate(prompt):
                    word = re.sub(r'[^a-zA-Z]', "", word)
                    if word in BANNED_WORDS:
                        if self.restricted:
                            raise InvalidWord(f"Banned word found: {word}")
                        else:
                            prompt[i] = prompt[i].replace(word, get_word(word))

                data["prompt"] = " ".join(prompt)

            # any to str
            data = {key: str(value) if type(value) != tuple else value for key, value in data.items()}

            multi = MultipartEncoder(fields=data)
            headers["content-type"] = multi.content_type
            data = multi.read()

        r = requests.request(
            method=kwargs.get("method", "GET"),
            url=kwargs.get("url"),
            data=data,
            headers=headers,
            timeout=60
        )
        r.raise_for_status()
        return r

    def thumb(self, item: Union[Style, Inspiration, Mode]) -> bytes:
        href = item.value[2 if isinstance(item, Style) else 1]
        return bytes2png(self._request(method="GET", url=f"{self.cdn}/{href}").content)

    def inspire(self, inspiration: Inspiration = Inspiration.INSPIRATION_01) -> bytes:
        """Inspiration"""
        return self.sdprem(
            prompt=inspiration.value[0],
            style=next((item for item in Style if item.value[0] == inspiration.value[2]), Style.IMAGINE_V3),
            seed=inspiration.value[3])

    # @package k7.a;
    def variate(
            self,
            content: bytes,
            prompt: str,
            strength: float = 0.0,
            style: Style = Style.IMAGINE_V3
    ) -> bytes:
        """Character"""
        return bytes2png(self._request(
            method="POST",
            url=f"{self.api}/variate",
            data={
                "model_version": self.version,
                "prompt": prompt + style.value[3],
                "strength": strength,
                "style_id": style.value[0],
                "image": ("image.jpeg", content, "image/jpg")
            }
        ).content)

    def sdprem(
            self,
            prompt: str,
            negative: str = None,
            style: Style = Style.IMAGINE_V3,
            seed: int = None,
            ratio: Ratio = Ratio.RATIO_1X1,
            cfg: float = 9.5,
            priority: bool = True,
            high_result: bool = False
    ) -> bytes:
        """AI Art"""
        return bytes2png(self._request(
            method="POST",
            url=f"{self.api}/sdprem",  # /sdprem (premium), /sd (free)
            data={
                "model_version": self.version,
                "prompt": prompt + style.value[3],
                "style_id": style.value[0],
                "aspect_ratio": ratio.value,
                "seed": seed,
                "cfg": get_cfg(cfg),
                "negative_prompt": negative,
                "priority": int(priority),
                "high_res_results": int(high_result)
            }
        ).content)

    def upscale(self, content: bytes):
        """Upscale"""
        return bytes2png(self._request(
            method="POST",
            url=f"{self.api}/upscale",
            data={
                "model_version": self.version,
                "image": ("_", content, "image/jpg")
            }
        ).content)

    def translate(self, prompt: str) -> str:
        """Translate Prompt"""
        return self._request(
            method="POST",
            url=f"{self.api}/translate",
            data={
                "q": prompt,
                "source": detect(prompt),
                "target": "en"
            }
        ).json()["translatedText"]

    def interrogator(self, content: bytes) -> str:
        """Generate Prompt"""
        return self._request(
            method="POST",
            url=f"{self.api}/interrogator",
            data={
                "model_version": self.version,
                "image": ("prompt_generator_temp.jpeg", content, "image/jpg")
            }
        ).text

    def sdimg(
            self,
            content: bytes,
            prompt: str,
            negative: str = None,
            seed: int = None,
            cfg: float = 9.5
    ) -> bytes:
        """Inpainting"""
        return bytes2png(self._request(
            method="POST",
            url=f"{self.api}/sdimg",
            data={
                "model_version": self.version,
                "prompt": prompt,
                "negative_prompt": negative,
                "seed": seed,
                "cfg": get_cfg(cfg),
                "image": ("bitmap_final_edit.jpg", content, "image/jpg")
            }
        ).content)

    def controlnet(
            self,
            content: bytes,
            prompt: str,
            negative: str = None,
            strength: float = 0.0,
            cfg: float = 9.5,
            mode: Mode = Mode.SCRIBBLE,
            style: Style = Style.IMAGINE_V3,
            seed: str = None
    ) -> bytes:
        """Image Remix"""
        return bytes2png(self._request(
            method="POST",
            url=f"{self.api}/controlnet",
            data={
                "model_version": self.version,
                "prompt": prompt + style.value[3],
                "negative_prompt": negative,
                "strength": strength,
                "cfg": get_cfg(cfg),
                "control": mode.value[0],
                "style_id": style.value[0],
                "seed": seed,
                "image": ("bitmap_final_edit.jpg", content, "image/jpg")
            }
        ).content)

    def codeformer(self, content: bytes) -> bytes:
        """Face Fixed"""
        return bytes2png(self._request(
            method="POST",
            url=f"{self.api}/codeformer",
            data={
                "model_version": self.version,
                "image": ("tempImage.jpg", content, "image/jpg")
            }
        ).content)
