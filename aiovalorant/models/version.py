import datetime
import typing

import pydantic

__all__: typing.Sequence[str] = ("Version",)


class Version(pydantic.BaseModel):
    """Represents the version.

    Attributes:
        manifest_id (str): the manifest id
        branch (str): the branch
        version (str): the version
        build_version (str): the build version
        engine_version (str): the engine version
        riot_client_version (str): the riot client version
        build_date (<class 'datetime.datetime'>): the build date
    """

    manifest_id: str = pydantic.Field(alias="manifestId")
    branch: str
    version: str
    build_version: str = pydantic.Field(alias="buildVersion")
    engine_version: str = pydantic.Field(alias="engineVersion")
    riot_client_version: str = pydantic.Field(alias="riotClientVersion")
    build_date: datetime.datetime = pydantic.Field(alias="buildDate")
