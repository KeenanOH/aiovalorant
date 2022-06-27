import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Currency",)


class Currency(traits.Identifiable):
    """Represents a currency.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        display_name_singular (str): the singular display name
        display_icon (str): the display icon
        large_icon (str): the large icon
        asset_path (str): the asset path
    """

    display_name: str = pydantic.Field(alias="displayName")
    display_name_singular: str = pydantic.Field(alias="displayNameSingular")
    display_icon: str = pydantic.Field(alias="displayIcon")
    large_icon: str = pydantic.Field(alias="largeIcon")
