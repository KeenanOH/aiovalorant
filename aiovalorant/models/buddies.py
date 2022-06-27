import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Level", "Buddy")


class Level(traits.Identifiable):
    """Represents the level of a buddy.

    Attributes:
        uuid (str): the uuid
        charm_level (int): the charm level
        display_name (str): the display name
        display_icon (str): the display icon
        asset_path (str): the asset path
    """

    charm_level: int = pydantic.Field(alias="charmLevel")
    display_name: str = pydantic.Field(alias="displayName")
    display_icon: str = pydantic.Field(alias="displayIcon")


class Buddy(traits.Identifiable):
    """Represents a buddy.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        is_hidden_if_not_owned (bool): hidden if not owned
        theme_uuid (str): the theme uuid
        display_icon (str): the display icon
        asset_path (str): the asset path
        levels (list[Level]): the levels
    """

    display_name: str = pydantic.Field(alias="displayName")
    is_hidden_if_not_owned: bool = pydantic.Field(alias="isHiddenIfNotOwned")
    theme_uuid: typing.Optional[str] = pydantic.Field(alias="themeUuid")
    display_icon: typing.Optional[str] = pydantic.Field(alias="display_icon")
    levels: list[Level]
