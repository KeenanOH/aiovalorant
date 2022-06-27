import typing

import pydantic

from aiovalorant import traits

__all__: typing.Sequence[str] = ("LevelBorder",)


class LevelBorder(traits.Identifiable):
    """Represents a level border.

    Attributes:
        uuid (str): the uuid
        starting_level (int): the starting level
        level_number_appearance (str): the level number appearance
        small_player_card_appearance (str): the small player card appearance
        asset_path (str): the asset path
    """

    starting_level: int = pydantic.Field(alias="startingLevel")
    level_number_appearance: str = pydantic.Field(alias="levelNumberAppearance")
    small_player_card_appearance: str = pydantic.Field(
        alias="smallPlayerCardAppearance"
    )
