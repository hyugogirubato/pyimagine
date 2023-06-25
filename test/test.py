import os
import time
from enum import Enum
from pathlib import Path

import pyimagine
from pyimagine.constants import Style, Ratio, Model
from pick import pick

PARENT = Path(__file__).resolve().parent


class Mode(Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"


class Upscale(Enum):
    NO = False
    YES = True


if __name__ == "__main__":
    imagine = pyimagine.Imagine(restricted=False)

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

    option, _ = pick([model.name for model in list(Model)], "Model:")
    usr_model = Model[option]

    option, _ = pick([style.name for style in list(Style)], "Style:")
    usr_style = Style[option]

    option, _ = pick([ratio.name for ratio in list(Ratio)], "Ratio:")
    usr_ratio = Ratio[option]

    os.system("cls" if os.name == "nt" else "clear")
    print(f"I: PyImagine version {pyimagine.__version__}")
    print(f"I: Prompt: {usr_prompt}")
    print(f"I: Negative: {usr_negative}")
    print(f"I: Model: {usr_model.name}")
    print(f"I: Style: {usr_style.name}")
    print(f"I: Ratio: {usr_ratio.name}")

    img_data = imagine.sdprem(
        prompt=usr_prompt,
        model=usr_model,
        negative=usr_negative,
        style=None if usr_style == Style.NO_STYLE else usr_style,
        ratio=usr_ratio,
    )

    file = PARENT / f"imagine_{int(time.time())}.png"
    file.write_bytes(img_data)
    option, index = pick([upscale.name for upscale in list(Upscale)], "Upscale:")
    usr_upscale = Upscale[option]

    print(f"I: Upscale: {usr_upscale.name}")
    if usr_upscale.value:
        img_data = imagine.upscale(content=img_data)
        file.write_bytes(img_data)
