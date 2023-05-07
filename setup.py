"""Setup module"""

from setuptools import setup

with open("README.md", mode="r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="pyimagine",
    version="2.6.4",
    description="Python library to create Art with AI.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/hyugogirubato/pyimagine",
    author="hyugogirubato",
    author_email="hyugogirubato@gmail.com",
    license="GNU GPLv3",
    packages=["pyimagine"],
    install_requires=["requests", "langdetect", "requests-toolbelt"],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ]
)
