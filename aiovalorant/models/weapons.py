import typing

import pydantic

from aiovalorant import traits

__all__: typing.Sequence[str] = (
    "ADSStats",
    "AltShotgunStats",
    "AirBurstStats",
    "DamageRange",
    "WeaponStats",
    "GridPosition",
    "ShopData",
    "Chroma",
    "Level",
    "Skin",
    "WeaponSkin",
    "WeaponSkinChroma",
    "Weapon",
)


class ADSStats(pydantic.BaseModel):
    """Represents the ADS stats.

    Attributes:
        zoom_multiplier (float): the zoom multiplier
        fire_rate (float): the fire rate
        run_speed_multiplier (float): the run speed multiplier
        burst_count (int): the burst count
        first_bullet_accuracy (float): the first bullet accuracy
    """

    zoom_multiplier: float = pydantic.Field(alias="zoomMultiplier")
    fire_rate: float = pydantic.Field(alias="fireRate")
    run_speed_multiplier: float = pydantic.Field(alias="runSpeedMultiplier")
    burst_count: int = pydantic.Field(alias="burstCount")
    first_bullet_accuracy: float = pydantic.Field(alias="firstBulletAccuracy")


class AltShotgunStats(pydantic.BaseModel):
    """Represents the alt shotgun stats.

    Attributes:
        shotgun_pellet_count (int): the shotgun pellet count
        burst_rate (float): the burst rate
    """

    shotgun_pellet_count: int = pydantic.Field(alias="shotgunPelletCount")
    burst_rate: float = pydantic.Field(alias="burstRate")


class AirBurstStats(pydantic.BaseModel):
    """Represents the air burst stats.

    Attributes:
        shotgun_pellet_count (int): the shotgun pellet count
        burst_distance (float): the burst distance
    """

    shotgun_pellet_count: int = pydantic.Field(alias="shotgunPelletCount")
    burst_distance: float = pydantic.Field(alias="burstDistance")


class DamageRange(pydantic.BaseModel):
    """Represents the damage range.

    Attributes:
        range_start_meters (float): the range start meters
        range_end_meters (float): the range end meters
        head_damage (float): the head damage
        body_damage (float): the body damage
        leg_damage (float): the leg damage
    """

    range_start_meters: float = pydantic.Field(alias="rangeStartMeters")
    range_end_meters: float = pydantic.Field(alias="rangeEndMeters")
    head_damage: float = pydantic.Field(alias="headDamage")
    body_damage: float = pydantic.Field(alias="bodyDamage")
    leg_damage: float = pydantic.Field(alias="legDamage")


class WeaponStats(pydantic.BaseModel):
    """Represents the weapon stats.

    Attributes:
        fire_rate (float): the fire rate
        magazine_size (int): the magazine size
        run_speed_multiplier (float): the run speed multiplier
        equip_time_seconds (float): the equip time seconds
        reload_time_seconds (float): the reload time seconds
        first_bullet_accuracy (float): the first bullet accuracy
        shotgun_pellet_count (int): the shotgun pellet count
        wall_penetration (str): the wall penetration
        feature (str): the feature
        fire_mode (str): the fire mode
        alt_fire_type (str): the alt fire type
        ads_stats (ADSStats): the ads stats
        alt_shotgun_stats (AltShotgunStats): the alt shotgun stats
        air_burst_stats (AirBurstStats): the air burst stats
        damage_ranges (list[DamageRange]): the damage ranges
    """

    fire_rate: float = pydantic.Field(alias="fireRate")
    magazine_size: int = pydantic.Field(alias="magazineSize")
    run_speed_multiplier: float = pydantic.Field(alias="runSpeedMultiplier")
    equip_time_seconds: float = pydantic.Field(alias="equipTimeSeconds")
    reload_time_seconds: float = pydantic.Field(alias="reloadTimeSeconds")
    first_bullet_accuracy: float = pydantic.Field(alias="firstBulletAccuracy")
    shotgun_pellet_count: int = pydantic.Field(alias="shotgunPelletCount")
    wall_penetration: str = pydantic.Field(alias="wallPenetration")
    feature: typing.Optional[str]
    fire_mode: typing.Optional[str] = pydantic.Field(alias="fireMode")
    alt_fire_type: typing.Optional[str] = pydantic.Field(alias="altFireType")
    ads_stats: typing.Optional[ADSStats] = pydantic.Field(alias="adsStats")
    alt_shotgun_stats: typing.Optional[AltShotgunStats] = pydantic.Field(
        alias="altShotgunStats"
    )
    air_burst_stats: typing.Optional[AirBurstStats] = pydantic.Field(
        alias="airBurstStats"
    )
    damage_ranges: list[DamageRange] = pydantic.Field(alias="damageRanges")


class GridPosition(pydantic.BaseModel):
    """Represents a grid position.

    Attributes:
        row (int): the row
        column (int): the column
    """

    row: int
    column: int


class ShopData(pydantic.BaseModel):
    """Represents shop data.

    Attributes:
        cost (int): the cost
        category (str): the category
        category_text (str): the category text
        grid_position (GridPosition): the grid position
        can_be_trashed (bool): the can be trashed
        image (str): the image
        new_image (str): the new image
        new_image2 (str): the new image2
        asset_path (str): the asset path
    """

    cost: int
    category: str
    category_text: str = pydantic.Field(alias="categoryText")
    grid_position: typing.Optional[GridPosition] = pydantic.Field(alias="gridPosition")
    can_be_trashed: bool = pydantic.Field(alias="canBeTrashed")
    image: typing.Optional[str]
    new_image: typing.Optional[str] = pydantic.Field(alias="newImage")
    new_image_2: typing.Optional[str] = pydantic.Field(alias="newImage2")
    asset_path: str = pydantic.Field(alias="assetPath")


class Chroma(traits.Identifiable):
    """Represents a chroma.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        display_icon (str): the display icon
        full_render (str): the full render
        swatch (str): the swatch
        streamed_video (str): the streamed video
    """

    display_name: str = pydantic.Field(alias="displayName")
    display_icon: typing.Optional[str] = pydantic.Field(alias="displayIcon")
    full_render: str = pydantic.Field(alias="fullRender")
    swatch: typing.Optional[str]
    streamed_video: typing.Optional[str] = pydantic.Field(alias="streamedVideo")


class Level(traits.Identifiable):
    """Represents a level.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        level_item (str): the level item
        display_icon (str): the display icon
        streamed_video (str): the streamed video
    """

    display_name: typing.Optional[str] = pydantic.Field(alias="displayName")
    level_item: typing.Optional[str] = pydantic.Field(alias="levelItem")
    display_icon: typing.Optional[str] = pydantic.Field(alias="displayIcon")
    streamed_video: typing.Optional[str] = pydantic.Field(alias="streamedVideo")


class Skin(traits.Identifiable):
    """Represents a skin.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        theme_uuid (str): the theme uuid
        content_tier_uuid (str): the content tier uuid
        display_icon (str): the display icon
        wallpaper (str): the wallpaper
        chromas (list[Chroma]): the chromas
        levels (list[Level]): the levels
    """

    display_name: str = pydantic.Field(alias="displayName")
    theme_uuid: str = pydantic.Field(alias="themeUuid")
    content_tier_uuid: typing.Optional[str] = pydantic.Field(alias="contentTierUuid")
    display_icon: typing.Optional[str] = pydantic.Field(alias="displayIcon")
    wallpaper: typing.Optional[str]
    chromas: list[Chroma]
    levels: list[Level]


class WeaponSkin(Skin):
    """Represents a weapon skin.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        theme_uuid (str): the theme uuid
        content_tier_uuid (str): the content tier uuid
        display_icon (str): the display icon
        wallpaper (str): the wallpaper
        chromas (list[Chroma]): the chromas
        levels (list[Level]): the levels
    """


class WeaponSkinChroma(Chroma):
    """Represents a chroma.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        display_icon (str): the display icon
        full_render (str): the full render
        swatch (str): the swatch
        streamed_video (str): the streamed video
    """


class Weapon(traits.Identifiable):
    """Represents a weapon.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        category (str): the category
        default_skin_uuid (str): the default skin uuid
        display_icon (str): the display icon
        kill_stream_icon (str): the kill stream icon
        weapon_stats (WeaponStats): the weapon stats
        shop_data (ShopData): the shop data
    """

    display_name: str = pydantic.Field(alias="displayName")
    category: str
    default_skin_uuid: str = pydantic.Field(alias="defaultSkinUuid")
    display_icon: str = pydantic.Field(alias="displayIcon")
    kill_stream_icon: str = pydantic.Field(alias="killStreamIcon")
    weapon_stats: typing.Optional[WeaponStats] = pydantic.Field(alias="weaponStats")
    shop_data: typing.Optional[ShopData] = pydantic.Field(alias="shopData")
