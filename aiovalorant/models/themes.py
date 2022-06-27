import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Theme",)


class Theme(traits.Identifiable):
    """Represents a theme.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
        display_name (str): the display name
        display_icon (str): the display icon
        store_featured_image (str): the store featured image
    """

    display_name: str = pydantic.Field(alias="displayName")
    display_icon: typing.Optional[str] = pydantic.Field(alias="displayIcon")
    store_featured_image: typing.Optional[str] = pydantic.Field(
        alias="storeFeaturedImage"
    )
