import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("ContentTier",)


class ContentTier(traits.Identifiable):
    """Represents a content tier

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        dev_name (str): the dev name
        rank (int): the rank
        juice_value (int): the juice value
        juice_cost (int): the juice cost
        highlight_color (str): the highlight color
        display_icon (str): the display icon
        asset_path (str): the asset path
    """

    display_name: str = pydantic.Field(alias="displayName")
    dev_name: str = pydantic.Field(alias="devName")
    rank: int
    juice_value: int = pydantic.Field(alias="juiceValue")
    juice_cost: int = pydantic.Field(alias="juiceCost")
    highlight_color: str = pydantic.Field(alias="highlightColor")
    display_icon: str = pydantic.Field(alias="displayIcon")
