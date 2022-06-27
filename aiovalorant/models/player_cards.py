import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("PlayerCard",)


class PlayerCard(traits.Identifiable):
    """Represents a player card.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        is_hidden_if_not_owned (bool): the is hidden if not owned
        theme_uuid (str): the theme uuid
        display_icon (str): the display icon
        wide_art (str): the wide art
        large_art (str): the large art
    """

    display_name: str = pydantic.Field(alias="displayName")
    is_hidden_if_not_owned: bool = pydantic.Field(alias="isHiddenIfNotOwned")
    theme_uuid: typing.Optional[str] = pydantic.Field(alias="themeUuid")
    display_icon: str = pydantic.Field(alias="displayIcon")
    small_art: str = pydantic.Field(alias="displayIcon")
    wide_art: str = pydantic.Field(alias="wideArt")
    large_art: str = pydantic.Field(alias="largeArt")
