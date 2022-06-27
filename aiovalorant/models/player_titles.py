import typing

import pydantic

from aiovalorant import traits


__all__: typing.Sequence[str] = ("PlayerTitle",)


class PlayerTitle(traits.Identifiable):
    display_name: str = pydantic.Field(alias="displayName")
    title_text: typing.Optional[str] = pydantic.Field(alias="titleText")
    is_hidden_if_not_owned: bool = pydantic.Field(alias="isHiddenIfNotOwned")
