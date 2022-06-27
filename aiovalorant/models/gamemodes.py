import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = (
    "GameFeatureOverride",
    "GameRuleBoolOverride",
    "Gamemode",
    "GamemodeEquippable",
)


class GameFeatureOverride(pydantic.BaseModel):
    """Represents a gamemode.

    Attributes:
        feature_name (str): the feature name
        state (bool): the state
    """

    feature_name: str = pydantic.Field(alias="featureName")
    state: bool


class GameRuleBoolOverride(pydantic.BaseModel):
    """Represents a gamemode.

    Attributes:
        rule_name (str): the rule name
        state (bool): the state
    """

    rule_name: str = pydantic.Field(alias="ruleName")
    state: bool


class Gamemode(traits.Identifiable):
    """Represents a gamemode.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        duration (str): the duration
        allows_match_timeouts (str): the allows match timeouts
        is_team_voice_allowed (bool): if team voice is allowed
        is_minimap_hidden (bool): if the minimap is hidden
        orb_count (int): the orb count
        team_roles (list[str]): the team roles
        game_feature_overrides (list[GameFeatureOverride]): the game feature overrides
        game_rule_bool_overrides (list[GameRuleBoolOverride]): the game rule bool overrides
        display_icon (str): the display icon
        asset_path (str): the asset path
    """

    display_name: str = pydantic.Field(alias="displayName")
    duration: typing.Optional[str]
    allows_match_timeouts: str = pydantic.Field(alias="allowsMatchTimeouts")
    is_team_voice_allowed: bool = pydantic.Field(alias="isTeamVoiceAllowed")
    is_minimap_hidden: bool = pydantic.Field(alias="isMinimapHidden")
    orb_count: int = pydantic.Field(alias="orbCount")
    team_roles: typing.Optional[list[str]] = pydantic.Field(alias="teamRoles")
    game_feature_overrides: typing.Optional[list[GameFeatureOverride]] = pydantic.Field(
        alias="gameFeatureOverrides"
    )
    game_rule_bool_overrides: typing.Optional[
        list[GameRuleBoolOverride]
    ] = pydantic.Field(alias="gameRuleBoolOverrides")
    display_icon: typing.Optional[str] = pydantic.Field(alias="displayIcon")


class GamemodeEquippable(traits.Identifiable):
    """Represents a gamemode equippable.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        category (str): the category
        display_icon (str): the display icon
        kill_stream_icon (str): the kill stream icon
        asset_path (str): the asset path
    """

    display_name: str = pydantic.Field(alias="displayName")
    category: str
    display_icon: str = pydantic.Field(alias="displayIcon")
    kill_stream_icon: str = pydantic.Field(alias="killStreamIcon")
