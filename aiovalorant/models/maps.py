import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Location", "Callout", "Map")


class Location(pydantic.BaseModel):
    """Represents a location.

    Attributes:
        x (float): the x
        y (float): the y
    """

    x: float
    y: float


class Callout(pydantic.BaseModel):
    """Represents a callout.

    Attributes:
        region_name (str): the region name
        super_region_name (str): the super region name
        location (Location): the location
    """

    region_name: str = pydantic.Field(alias="regionName")
    super_region_name: str = pydantic.Field(alias="superRegionName")
    location: Location


class Map(traits.Identifiable):
    """Represents a map.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        coordinates (str): the coordinates
        display_icon (str): the display icon
        list_view_icon (str): the list view icon
        splash (str): the splash
        map_url (str): the map url
        x_multiplier (float): the x multiplier
        y_multiplier (float): the y multiplier
        x_scalar_to_add (float): the x scalar to add
        y_scalar_to_add (float): the y scalar to add
        callouts (list[Callout): the callouts
    """

    display_name: str = pydantic.Field(alias="displayName")
    coordinates: str
    display_icon: typing.Optional[str] = pydantic.Field(alias="displayIcon")
    list_view_icon: str = pydantic.Field(alias="listViewIcon")
    splash: str
    map_url: str = pydantic.Field(alias="mapUrl")
    x_multiplier: float = pydantic.Field(alias="xMultiplier")
    y_multiplier: float = pydantic.Field(alias="yMultiplier")
    x_scalar_to_add: float = pydantic.Field(alias="xScalarToAdd")
    y_scalar_to_add: float = pydantic.Field(alias="yScalarToAdd")
    callouts: typing.Optional[list[Callout]]
