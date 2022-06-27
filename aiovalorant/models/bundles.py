import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("Bundle",)


class Bundle(traits.Identifiable):
    """Represents a bundle.

    Attributes:
        uuid (str): the uuid
        display_name (str): the display name
        display_name_sub_text (str): the display name sub text
        description (str): the description
        extra_description (str): the extra description
        promo_description (str): the promo description
        use_additional_context (bool): the addition use context
        display_icon (str): the display icon
        display_icon_2 (str): the second display icon
        vertical_promo_image (str): the vertical promotion image
        asset_path (str): the asset path
    """

    display_name: str = pydantic.Field(alias="displayName")
    display_name_sub_text: typing.Optional[str] = pydantic.Field(
        alias="displayNameSubText"
    )
    description: str
    extra_description: typing.Optional[str] = pydantic.Field(alias="extraDescription")
    promo_description: typing.Optional[str] = pydantic.Field(alias="promo_description")
    use_additional_context: bool = pydantic.Field(alias="useAdditionalContext")
    display_icon: str = pydantic.Field(alias="displayIcon")
    display_icon_2: str = pydantic.Field(alias="displayIcon2")
    vertical_promo_image: typing.Optional[str] = pydantic.Field(
        alias="verticalPromoImage"
    )
