<div align="center">

<img src="https://github.com/hyugogirubato/pyimagine/blob/main/docs/images/icon.png" width="10%">

# PyImagine

[![License](https://img.shields.io/github/license/hyugogirubato/pyimagine)](https://github.com/hyugogirubato/pyimagine/blob/main/LICENSE)
[![Release](https://img.shields.io/github/release-date/hyugogirubato/pyimagine)](https://github.com/hyugogirubato/pyimagine/releases)
[![Latest Version](https://img.shields.io/pypi/v/pyimagine)](https://pypi.org/project/pyimagine/)

</div>


PyImagine is a Python library for AI-powered image manipulation. It provides a simple interface to interact with an
image manipulation service, allowing you to perform various operations on images.

## Features

- Generate inspired images based on predefined prompts and styles.
- Apply variations to images based on prompts, strengths, and styles.
- Enhance image resolution and quality using AI-powered upscaling.
- Generate prompts based on the content of images.
- Fill in missing or corrupted parts of images.
- Remix images by applying control prompts, strengths, and styles.
- Fix and enhance facial features in images.

## Installation

You can install PyImagine using pip:

````shell
pip install pyimagine
````

## Usage

Here's a basic example of how to use PyImagine:

````python
from pyimagine import Arta
from pyimagine.constants import Style

# Initialize Imagine
arta = Arta()
arta.signupNewUser()

# Generate from inspiration
inspired_image = arta.infer(prompt="Create something amazing!", style=Style.REALISTIC_2)

# Prompt from image
original_image = open('image.jpg', 'rb').read()
prompt_image = arta.image2text(original_image, language_code='en')

# And more...
````

For more information on how to use PyImagine, please refer to
the [documentation](https://github.com/hyugogirubato/pyimagine/blob/main/docs).

## Disclaimer

PyImagine is an unofficial library and is not affiliated with or endorsed by Vyroai or Aiby. The library is provided "as
is" without any warranty, and the usage of this library is at your own risk. Make sure to comply with the terms and
conditions of the Imagine service while using this library.

### License

This project is licensed under the [GPL v3 License](https://github.com/hyugogirubato/pyimagine/blob/main/LICENSE).
