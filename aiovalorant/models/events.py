import datetime
import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Event",)


class Event(traits.Identifiable):
    """Represents an event.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        short_display_name (str): the short display name
        start_time (datetime.datetime): the start time
        end_time (datetime.datetime): the end time
        asset_path (str): the asset path
    """

    display_name: str = pydantic.Field(alias="displayName")
    short_display_name: str = pydantic.Field(alias="shortDisplayName")
    start_time: datetime.datetime = pydantic.Field(alias="startTime")
    end_time: datetime.datetime = pydantic.Field(alias="endTime")
