import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Role", "Ability", "MediaList", "VoiceLine", "Agent")


class Role(pydantic.BaseModel):
    """Represents an agent's role.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        description (str): the description
        display_icon (str): the display icon
    """

    uuid: str
    display_name: str = pydantic.Field(alias="displayName")
    description: str
    display_icon: str = pydantic.Field(alias="displayIcon")


class Ability(pydantic.BaseModel):
    """Represents an agent's ability.

    Attributes:
        slot (str): the slot
        display_name (str): the display name
        description (str): the description
        display_icon (typing.Optional[str]): the display icon
    """

    slot: str
    display_name: str = pydantic.Field(alias="displayName")
    description: str
    display_icon: typing.Optional[str] = pydantic.Field(alias="displayIcon")


class MediaList(pydantic.BaseModel):
    """Represents a media list from an agent's voiceline.

    Attributes:
        id (str): the id
        wwise (str): the wwise
        wave (str): the wave
    """

    id: int
    wwise: str
    wave: str


class VoiceLine(pydantic.BaseModel):
    """Represents an agent's voice line.

    Attributes:
        min_duration (float): the minimum duration
        max_duration (float): the maximum duration
        media_list (list[MediaList]): the media list
    """

    min_duration: float = pydantic.Field(alias="minDuration")
    max_duration: float = pydantic.Field(alias="maxDuration")
    media_list: list[MediaList] = pydantic.Field(alias="mediaList")


class Agent(traits.Identifiable):
    """Represents a Valorant agent.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        description (str): the description
        developer_name (str): the developer's name
        character_tags (typing.Optional[list[str]]): the character tags
        display_icon (str): the display icon
        display_icon_small (str): the small display icon
        bust_portrait (typing.Optional[str]): the bust portrait
        full_portrait (typing.Optional[str]): the full portrait
        full_portrait_v2 (typing.Optional[str]): the second full portrait
        kill_feed_portrait (str): the kill feed portrait
        background (typing.Optional[str]): the background
        background_gradient_colors (typing.Optional[list[str]]): the background gradient colors
        asset_path (str): the asset path
        is_full_portrait_right_facing (bool): if the portrait is right facing
        is_playable_charcter (bool): if the character can be played
        is_available_for_test (bool): if the agent is avaliable for test
        is_base_content (bool): if the agent is base content
        role (typing.Optional[Role]): the agent's role
        abilities (typing.Optional[Abiity]): the agent's abilities
        voice_line (typing.Optional[VoiceLine]): the agent's voice line
    """

    display_name: str = pydantic.Field(alias="displayName")
    description: str
    developer_name: str = pydantic.Field(alias="developerName")
    character_tags: typing.Optional[list[str]] = pydantic.Field(alias="characterTags")
    display_icon: str = pydantic.Field(alias="displayIcon")
    display_icon_small: str = pydantic.Field(alias="displayIconSmall")
    bust_portrait: typing.Optional[str] = pydantic.Field(alias="bustPortrait")
    full_portrait: typing.Optional[str] = pydantic.Field(alias="fullPortrait")
    full_portrait_v2: typing.Optional[str] = pydantic.Field(alias="fullPortraitV2")
    kill_feed_portrait: str = pydantic.Field(alias="killfeedPortrait")
    background: typing.Optional[str]
    background_gradient_colors: typing.Optional[list[str]] = pydantic.Field(
        alias="backgroundGradientColors"
    )
    is_full_portrait_right_facing: bool = pydantic.Field(
        alias="isFullPortraitRightFacing"
    )
    is_playable_character: bool = pydantic.Field(alias="isPlayableCharacter")
    is_available_for_test: bool = pydantic.Field(alias="isAvailableForTest")
    is_base_content: bool = pydantic.Field(alias="isBaseContent")
    role: typing.Optional[Role]
    abilities: typing.Optional[list[Ability]]
    voice_line: typing.Optional[VoiceLine]
