import typing

__all__: typing.Sequence[str] = (
    "ValorantAPIException",
    "MissingOrInvalidParameters",
    "DoesNotExist",
)


class ValorantAPIException(Exception):
    """The base exception for an API error."""


class MissingOrInvalidParameters(ValorantAPIException):
    """When one of the parameters is invalid or missing."""


class DoesNotExist(ValorantAPIException):
    """The object tied to the uuid does not exist."""
