class PyImagineException(Exception):
    """Exceptions used by pyimagine."""


class InvalidWord(PyImagineException):
    """Used word is invalid."""


class InvalidSize(PyImagineException):
    """Both sizes must be the same."""


class BannedContent(PyImagineException):
    """Content wanting to be generated is banned."""
