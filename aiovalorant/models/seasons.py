import datetime
import typing

import pydantic

from aiovalorant import traits

__all__: typing.Sequence[str] = (
    "Season",
    "Border",
    "CompetitiveSeason",
)


class Season(traits.Identifiable):
    """Represents a season.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        type (str): the type
        start_time (datetime.datetime): the start time
        end_time (datetime.datetime): the end time
        parent_uuid (str): the parent uuid
    """

    display_name: str = pydantic.Field(alias="displayName")
    type: typing.Optional[str]
    start_time: datetime.datetime = pydantic.Field(alias="startTime")
    end_time: datetime.datetime = pydantic.Field(alias="endTime")
    parent_uuid: typing.Optional[str] = pydantic.Field(alias="parentUuid")


class Border(traits.Identifiable):
    """Represents a border.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        level (int): the level
        wins_required (int): the wins required
        display_icon (str): the display icon
        small_icon (str): the small icon
    """

    level: int
    wins_required: int = pydantic.Field(alias="winsRequired")
    display_icon: str = pydantic.Field(alias="displayIcon")
    small_icon: typing.Optional[str] = pydantic.Field(alias="smallIcon")


class CompetitiveSeason(traits.Identifiable):
    """Represents a competitive season.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        start_time (datetime.datetime): the start time
        end_time (datetime.datetime): the end time
        season_uuid (str): the season uuid
        competitive_tiers_uuid (str): the competitive tiers uuid
        borders (list[Border): the borders
    """

    start_time: datetime.datetime = pydantic.Field(alias="startTime")
    end_time: datetime.datetime = pydantic.Field(alias="endTime")
    season_uuid: str = pydantic.Field(alias="seasonUuid")
    competitive_tiers_uuid: str = pydantic.Field(alias="competitiveTiersUuid")
    borders: typing.Optional[list[Border]]
