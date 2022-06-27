import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Level", "Spray", "SprayLevel")


class Level(traits.Identifiable):
    """Represnts a level.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        spray_level (int): the spray level
        display_name (str): the display name
        display_icon (str): the display icon
    """

    spray_level: int = pydantic.Field(alias="sprayLevel")
    display_name: str = pydantic.Field(alias="displayName")
    display_icon: str = pydantic.Field(alias="displayIcon")


class Spray(traits.Identifiable):
    """Represents a spray.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        category (str): the category
        theme_uuid (str): the theme uuid
        display_icon (str): the display icon
        full_icon (str): the full icon
        full_transparent_icon (str): the full transparent icon
        levels (list[Level]): the levels
    """

    display_name: str = pydantic.Field(alias="displayName")
    category: typing.Optional[str]
    theme_uuid: typing.Optional[str] = pydantic.Field(alias="themeUuid")
    display_icon: str = pydantic.Field(alias="displayIcon")
    full_icon: typing.Optional[str] = pydantic.Field(alias="fullIcon")
    full_transparent_icon: typing.Optional[str] = pydantic.Field(
        alias="fullTransparentIcon"
    )
    levels: list[Level]


class SprayLevel(Level):
    """Represnts a spray level.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        spray_level (int): the spray level
        display_name (str): the display name
        display_icon (str): the display icon
    """
