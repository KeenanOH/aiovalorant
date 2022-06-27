import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Tier", "CompetitiveTier")


class Tier(pydantic.BaseModel):
    """Represents a tier.

    Attributes:
        tier (int): the tier
        tier_name (str): the tier name
        division (str): the division
        division_name (str): the division name
        color (str): the color
        background_color (str): the background color
        small_icon (str): the small icon
        large_icon (str): the large icon
        rank_triangle_down_icon (str): the rank triangle down icon
        rank_triangle_up_icon (str): the rank triangle up icon
    """

    tier: int
    tier_name: typing.Optional[str]
    division: str
    division_name: str = pydantic.Field(alias="divisionName")
    color: str
    background_color: str = pydantic.Field(alias="backgroundColor")
    small_icon: typing.Optional[str] = pydantic.Field(alias="smallIcon")
    large_icon: typing.Optional[str] = pydantic.Field(alias="largeIcon")
    rank_triangle_down_icon: typing.Optional[str] = pydantic.Field(
        alias="rankTriangleDownIcon"
    )
    rank_triangle_up_icon: typing.Optional[str] = pydantic.Field(
        alias="rankTriangleUpIcon"
    )


class CompetitiveTier(traits.Identifiable):
    """Represents a competitive tier.

    Attributes:
        uuid (str): the uuid
        asset_object_name (str): the asset object name
        tiers (list[Tier]): the tiers
        asset_path (str): the asset path
    """

    asset_object_name: str = pydantic.Field(alias="assetObjectName")
    tiers: list[Tier]
