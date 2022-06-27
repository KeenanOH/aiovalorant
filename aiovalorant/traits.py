import pydantic


class Identifiable(pydantic.BaseModel):
    """Represents an object with an uuid and asset path.

    Attributes:
        uuid (str): the uuid
        asset_path (str): the asset path
    """

    uuid: str
    asset_path: str = pydantic.Field(alias="assetPath")
