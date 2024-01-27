import os
from enum import Enum

from pathlib import Path

import requests
from pick import pick

import pyimagine
from pyimagine.aiby import Arta
from pyimagine.constants import Style, Ratio

PARENT = Path('.')


class Mod(Enum):
    MANUAL = 'manual'
    AUTOMATIC = 'automatic'


class Upscale(Enum):
    YES = True
    NO = False


if __name__ == '__main__':
    arta = Arta(restricted=False)
    arta.signupNewUser()

    option, index = pick([m.name for m in list(Mod)], 'Mod')
    usr_mode = Mod[option]

    if usr_mode == Mod.MANUAL:
        usr_prompt = input('Prompt: ')
    else:
        path = Path(input('Image: '))
        if not path.is_file():
            raise FileNotFoundError(path)
        usr_prompt = arta.image2text(path.read_bytes(), language_code='en')

    usr_negative = input('Negative: ')

    option, _ = pick([s.name for s in list(Style)], 'Style')
    usr_style = Style[option]

    option, _ = pick([r.name for r in list(Ratio)], 'Ratio')
    usr_ratio = Ratio[option]

    option, index = pick([u.name for u in list(Upscale)], 'Upscale')
    usr_upscale = Upscale[option]

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'I: PyImagine version {pyimagine.__version__}')
    print(f'I: Prompt: {usr_prompt}')
    print(f'I: Negative: {usr_negative}')
    print(f'I: Style: {usr_style.name}')
    print(f'I: Ratio: {usr_ratio.name}')
    print(f'I: Upscale: {usr_upscale.name}')

    img_url = arta.infer(
        prompt=usr_prompt,
        negative_prompt=usr_negative,
        style=usr_style,
        aspect_ratio=usr_ratio,
        images_num=1,
        image_upscale=usr_upscale.value
    )[0]
    print(f'I: Url: {img_url}')

    img_path = PARENT / Path(img_url).name
    img_path.write_bytes(requests.request(method='GET', url=img_url).content)
    print(f'I: Path: {img_path}')
