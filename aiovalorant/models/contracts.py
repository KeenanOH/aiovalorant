import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = (
    "Reward",
    "Level",
    "FreeReward",
    "Chapter",
    "Content",
    "Contract",
)


class Reward(pydantic.BaseModel):
    """Represents a reward.

    Attributes:
        type (str): the type
        uuid (str): the uuid
        amount (int): the amount
        is_highlighted (bool): if it is highlighted
    """

    type: str
    uuid: str
    amount: int
    is_highlighted: bool = pydantic.Field(alias="isHighlighted")


class Level(pydantic.BaseModel):
    """Represents a level.

    Attributes:
        reward (Reward): the reward
        xp (int): the xp
        vp_cost (int): the vp cost
        is_purchasable_with_vp (typing.Optional[bool]): if it can be purchased with vp
    """

    reward: Reward
    xp: int
    vp_cost: int = pydantic.Field(alias="vpCost")
    is_purchasable_with_vp: typing.Optional[bool] = pydantic.Field(
        alias="isPurchasableWithVP "
    )


class FreeReward(pydantic.BaseModel):
    """Represents a free reward.

    Attributes:
        type (str): the type
        uuid (str): the uuid
        amount (int): the amount
        is_highlighted (bool): if it is highlighted
    """

    type: str
    uuid: str
    amount: int
    is_highlighted: bool = pydantic.Field(alias="isHighlighted")


class Chapter(pydantic.BaseModel):
    """Represents a chapter.

    Attributes:
        is_epilogue (bool): if it is an epilogue
        levels (list[Level]): the levels
        free_rewards (list[FreeReward]): the free rewards
    """

    is_epilogue: bool = pydantic.Field(alias="isEpilogue")
    levels: list[Level]
    free_rewards: typing.Optional[list[FreeReward]] = pydantic.Field(
        alias="freeRewards"
    )


class Content(pydantic.BaseModel):
    """Represents content.

    Attributes:
        relation_type (str): the relation type
        relation_uuid (str): the relation uuid
        chapters (list[Chapter]): the chapters
        premium_reward_schedule_uuid (str): the premium reward schedule uuid
        premium_vp_cost (int): the premium vp cost
    """

    relation_type: typing.Optional[str] = pydantic.Field(alias="relationType")
    relation_uuid: typing.Optional[str] = pydantic.Field(alias="relationUuid")
    chapters: list[Chapter]
    premium_rewards_schedule_uuid: typing.Optional[str] = pydantic.Field(
        alias="premiumRewardScheduleUuid"
    )
    premium_vp_cost: int = pydantic.Field(alias="premiumVPCost")


class Contract(traits.Identifiable):
    """Represents a contract.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        display_icon (str): the display icon
        ship_it (bool): the ship it
        free_reward_schedule_uuid (str): the free reward schedule uuid
        content (Content): the content
        asset_path (str): the asset path
    """

    display_name: str = pydantic.Field(alias="displayName")
    display_icon: typing.Optional[str] = pydantic.Field(alias="displayIcon")
    ship_it: bool = pydantic.Field(alias="shipIt")
    free_reward_schedule_uuid: typing.Optional[str] = pydantic.Field(
        alias="freeRewardScheduleUuid"
    )
    content: Content
