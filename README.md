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
from pyimagine import Imagine
from pyimagine.constants import Inspiration

# Initialize Imagine
imagine = Imagine()

# Generate an inspired image
inspired_image = imagine.sdinsp(Inspiration.INSPIRATION_01)

# Variate an image
original_image = open("image.jpg", "rb").read()
variated_image = imagine.variate(original_image, prompt="Create something amazing!")

# Upscale an image
upscaled_image = imagine.upscale(original_image)

# And more...
````

For more information on how to use PyImagine, please refer to
the [documentation](https://github.com/hyugogirubato/pyimagine/blob/main/docs).

### Exceptions

The following exceptions can be raised by PyImagine:

- `InvalidWord`: Raised when a banned word is found in the prompt. By default, if the `restricted` flag is set to `True`
  during initialization, the library will raise an `InvalidWord` exception. You can customize this behavior by setting
  `restricted` to `False` to replace banned words with alternative words instead of raising an exception.
- `InvalidSize`: Raised when attempting to perform an operation that requires both images to have the same size.

## Disclaimer

PyImagine is an unofficial library and is not affiliated with or endorsed by Imagine or Vyroai. The library is
provided "as is" without any warranty, and the usage of this library is at your own risk. Make sure to comply with the
terms and conditions of the Imagine service while using this library.

### License

This project is licensed under the [GPL v3 License](https://github.com/hyugogirubato/pyimagine/blob/main/LICENSE).
