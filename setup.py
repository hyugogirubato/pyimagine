from setuptools import setup, find_packages

setup(
    name='pyimagine',
    version='3.3.8',
    author='hyugogirubato',
    author_email='hyugogirubato@gmail.com',
    description='Python library for AI-powered image manipulation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hyugogirubato/pyimagine',
    packages=find_packages(),
    license='GPL-3.0-only',
    keywords=[
        'art',
        'image',
        'ai',
        'stable-diffusion'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities'
    ],
    install_requires=[
        'requests',
        'requests_toolbelt'
    ],
    python_requires='>=3.7'
)
