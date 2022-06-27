import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Ceremony",)


class Ceremony(traits.Identifiable):
    """Represents a ceremony.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        asset_path (str): the asset path
    """

    display_name: str = pydantic.Field(alias="displayName")
