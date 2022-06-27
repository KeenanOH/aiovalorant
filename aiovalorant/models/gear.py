import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = (
    "GridPosition",
    "ShopData",
    "Gear",
)


class GridPosition(pydantic.BaseModel):
    """Represents the shop data.

    Attributes:
        row (int): the row
        column (int): the column
    """

    row: int
    column: int


class ShopData(pydantic.BaseModel):
    """Represents the shop data.

    Attributes:
        cost (int): the cost
        category (str): the category
        category_text (str): the category text
        grid_position (GridPosition): the grid position
        can_be_trashed (bool): if it can be trashed
        image (str): the image
        new_image (str): the new image
        new_image2 (str): the new second image
        asset_path (str): the asset path
    """

    cost: int
    category: str
    category_text: str = pydantic.Field(alias="categoryText")
    grid_position: typing.Optional[GridPosition]
    can_be_trashed: bool = pydantic.Field(alias="canBeTrashed")
    image: typing.Optional[str]
    new_image: str = pydantic.Field(alias="newImage")
    new_image_2: typing.Optional[str] = pydantic.Field(alias="newImage2")
    asset_path: str = pydantic.Field(alias="assetPath")


class Gear(traits.Identifiable):
    """Represents gear.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        description (str): the description
        display_icon (str): the display icon
        asset_path (str): the asset path
        shop_data (ShopData): the shop data
    """

    display_name: str = pydantic.Field(alias="displayName")
    description: str
    display_icon: str = pydantic.Field(alias="displayIcon")
    shop_data: ShopData = pydantic.Field(alias="shopData")
