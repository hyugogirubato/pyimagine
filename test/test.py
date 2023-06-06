import os
from enum import Enum
from pathlib import Path

import pyimagine
from pyimagine.constants import Style, Ratio
from pick import pick

FILE = Path(__file__).resolve().parent / "imagine.png"


class Mode(Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"


class Upscale(Enum):
    NO = False
    YES = True


if __name__ == "__main__":
    imagine = pyimagine.Imagine(restricted=True)

    option, index = pick([mode.name for mode in list(Mode)], "Mode:")
    usr_mode = Mode[option]

    if usr_mode == Mode.MANUAL:
        usr_prompt = input("Prompt: ")
    else:
        path_image = Path(input("Image: "))
        if not path_image.exists() and not path_image.is_file():
            raise Exception(f"Error: File path is invalid, {path_image}")
        usr_prompt = imagine.interrogator(content=open(path_image, mode="rb").read())

    usr_negative = input("Negative: ")

    option, index = pick([style.name for style in list(Style)], "Style:")
    usr_style = Style[option]

    option, index = pick([ratio.name for ratio in list(Ratio)], "Ratio:")
    usr_ratio = Ratio[option]

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"I: PyImagine version {pyimagine.__version__}")
    print(f"I: Prompt: {usr_prompt}")
    print(f"I: Negative: {usr_negative}")
    print(f"I: Style: {usr_style.name}")
    print(f"I: Ratio: {usr_ratio.name}")

    img_data = imagine.sdprem(
        prompt=usr_prompt,
        negative=usr_negative,
        style=usr_style,
        ratio=usr_ratio
    )

    FILE.write_bytes(img_data)
    option, index = pick([upscale.name for upscale in list(Upscale)], "Upscale:")
    usr_upscale = Upscale[option]

    print(f"I: Upscale: {usr_upscale.name}")
    if usr_upscale.value:
        img_data = imagine.upscale(content=img_data)
        FILE.write_bytes(img_data)
