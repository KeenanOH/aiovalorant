import typing
from urllib import parse

import aiosonic
import pydantic

from aiovalorant import exceptions
from aiovalorant.models import *

__all__: typing.Sequence[str] = ("Client",)


class Client:
    def __init__(
        self, http_client: aiosonic.HTTPClient = aiosonic.HTTPClient()
    ) -> None:
        """Initializes the API client.

        Args:
            http_client (aiosonic.HTTPClient): The http client to use
        """
        self._http_client: aiosonic.HTTPClient = http_client
        self._base_url: str = "https://valorant-api.com/v1"

    async def _handle_request(
        self,
        endpoint: str,
        model: typing.Type[typing.Union[pydantic.BaseModel, list[pydantic.BaseModel]]],
        **kwargs,
    ) -> typing.Any:
        response: aiosonic.HttpResponse = await self._http_client.get(
            self._add_parameters(f"{self._base_url}{endpoint}", **kwargs)
        )
        response_json: dict[str, typing.Any] = await response.json()
        if response_json["status"] == 200:
            return pydantic.parse_obj_as(model, response_json["data"])

        if response_json["status"] == 400:
            raise exceptions.MissingOrInvalidParameters(response_json["error"])
        elif response_json["status"] == 404:
            raise exceptions.DoesNotExist(response_json["error"])
        raise exceptions.ValorantAPIException(response_json["error"])

    @staticmethod
    def _to_camel_case(string: str) -> str:
        components: list[str] = string.split("_")
        return components[0] + "".join(x.title() for x in components[1:])

    @staticmethod
    def _add_parameters(endpoint: str, **kwargs) -> str:
        for key, value in kwargs.copy().items():
            if not value:
                del kwargs[key]

        if len(kwargs) >= 1:
            return f"{endpoint}?{parse.urlencode(kwargs)}"
        return endpoint

    async def get_agents(
        self,
        language: typing.Optional[str] = None,
        is_playable_character: typing.Optional[bool] = None,
    ) -> list[agents.Agent]:
        """Gets the agents.

        Args:
            language (typing.Optional[str]): the language
            is_playable_character (typing.Optional[bool]): if the agent can be used

        Returns:
            list[agents.Agent]: a list of the agents
        """
        return await self._handle_request(
            "/agents",
            list[agents.Agent],
            language=language,
            is_playable_character=is_playable_character,
        )

    async def get_agent_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> agents.Agent:
        """Gets an agent by the UUID.

        Args:
            uuid (str): the agent's uuid
            language (typing.Optional[str]): the language

        Returns:
            agents.Agent: the agent
        """
        return await self._handle_request(
            f"/agents/{uuid}", agents.Agent, language=language
        )

    async def get_buddies(
        self, language: typing.Optional[str] = None
    ) -> list[buddies.Buddy]:
        """Gets the buddies.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[buddies.Buddy]: a list of the buddies
        """
        return await self._handle_request(
            "/buddies", list[buddies.Buddy], language=language
        )

    async def get_buddy_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> buddies.Buddy:
        """Gets a buddy by the uuid.

        Args:
            uuid (str): the buddy's uuid
            language (typing.Optional[str]): the language

        Returns:
            buddies.Buddy: the buddy
        """
        return await self._handle_request(
            f"/buddies/{uuid}", buddies.Buddy, language=language
        )

    async def get_bundles(
        self, language: typing.Optional[str] = None
    ) -> list[bundles.Bundle]:
        """Gets the bundles.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[bundles.Bundle]: a list of the bundles
        """
        return await self._handle_request(
            "/bundles", list[bundles.Bundle], language=language
        )

    async def get_bundle_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> bundles.Bundle:
        """Gets a bundle by its uuid.

        Args:
            uuid (str): the bundle's uuid
            language (typing.Optional[str]): the language

        Returns:
            bundles.Bundle: the bundle
        """
        return await self._handle_request(
            f"/bundles/{uuid}", bundles.Bundle, language=language
        )

    async def get_ceremonies(
        self, language: typing.Optional[str] = None
    ) -> list[ceremonies.Ceremony]:
        """Gets the ceremonies.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[ceremonies.Ceremony]: a list of the ceremonies
        """
        return await self._handle_request(
            f"/ceremonies", list[ceremonies.Ceremony], language=language
        )

    async def get_ceremony_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> ceremonies.Ceremony:
        """Gets a ceremony by its uuid.

        Args:
            uuid (str): the ceremony's uuid
            language (typing.Optional[str]): the language

        Returns:
            ceremonies.Ceremony: the ceremony
        """
        return await self._handle_request(
            f"/ceremonies/{uuid}", ceremonies.Ceremony, language=language
        )

    async def get_competitive_tiers(
        self, language: typing.Optional[str] = None
    ) -> list[competitive_tiers.CompetitiveTier]:
        """Gets the competitive tiers.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[competitive_tiers.CompetitiveTier]: a list of the competitive tiers
        """
        return await self._handle_request(
            "/competitivetiers",
            list[competitive_tiers.CompetitiveTier],
            language=language,
        )

    async def get_competitive_tier_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> competitive_tiers.CompetitiveTier:
        """Gets a competitive tier by its uuid.

        Args:
            uuid (str): the competitive tier's uuid
            language (typing.Optional[str]): the language

        Returns:
            competitive_tiers.CompetitiveTier: the competitive tier
        """
        return await self._handle_request(
            f"/competitivetiers/{uuid}",
            competitive_tiers.CompetitiveTier,
            language=language,
        )

    async def get_content_tiers(
        self, language: typing.Optional[str] = None
    ) -> list[content_tiers.ContentTier]:
        """Gets the content tiers.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[content_tiers.ContentTier]: a list of the content tiers
        """
        return await self._handle_request(
            "/contenttiers", list[content_tiers.ContentTier], language=language
        )

    async def get_content_tier_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> content_tiers.ContentTier:
        """Gets a content tier by its uuid.

        Args:
            uuid (str): the content tier's uuid
            language (typing.Optional[str]): the language

        Returns:
            content_tiers.ContentTier: the content tier
        """
        return await self._handle_request(
            f"/contenttiers/{uuid}", content_tiers.ContentTier, language=language
        )

    async def get_contracts(
        self, language: typing.Optional[str] = None
    ) -> list[contracts.Contract]:
        """Gets the contracts.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[contracts.Contract]: a list of the contracts
        """
        return await self._handle_request(
            "/contracts", list[contracts.Contract], language=language
        )

    async def get_contract_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> contracts.Contract:
        """Gets a contract by its uuid.

        Args:
            uuid (str): the contract's uuid
            language (typing.Optional[str]): the language

        Returns:
            contracts.Contract: the contract
        """
        return await self._handle_request(
            f"/contracts/{uuid}", contracts.Contract, language=language
        )

    async def get_currencies(
        self, language: typing.Optional[str] = None
    ) -> list[currencies.Currency]:
        """Gets the currencies.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[currencies.Currency]: a list of the currencies
        """
        return await self._handle_request(
            "/currencies", list[currencies.Currency], language=language
        )

    async def get_currency_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> currencies.Currency:
        """Gets a currency by its uuid.

        Args:
            uuid (str): the currency's uuid
            language (str): the language

        Returns:
            currencies.Curreny: the currency
        """
        return await self._handle_request(
            f"/currencies/{uuid}", currencies.Currency, language=language
        )

    async def get_events(
        self, language: typing.Optional[str] = None
    ) -> list[events.Event]:
        """Gets the events.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[events.Event]: a list of the events
        """
        return await self._handle_request(
            "/events", list[events.Event], language=language
        )

    async def get_event_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> events.Event:
        """Gets a event by its uuid.

        Args:
            uuid (str): the event's uuid
            language (str): the language

        Returns:
            events.Event: the event
        """
        return await self._handle_request(
            f"/events/{uuid}", events.Event, language=language
        )

    async def get_gamemodes(
        self, language: typing.Optional[str] = None
    ) -> list[gamemodes.Gamemode]:
        """Gets the gamemodes.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[gamemodes.Gamemode]: a list of the gamemodes
        """
        return await self._handle_request(
            "/gamemodes", list[gamemodes.Gamemode], language=language
        )

    async def get_gamemode_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> gamemodes.Gamemode:
        """Gets a gamemode by its uuid.

        Args:
            uuid (str): the gamemode's uuid
            language (str): the language

        Returns:
            gamemodes.Gamemode: the gamemode
        """
        return await self._handle_request(
            f"/gamemodes/{uuid}", gamemodes.Gamemode, language=language
        )

    async def get_gamemode_equippables(
        self, language: typing.Optional[str] = None
    ) -> list[gamemodes.GamemodeEquippable]:
        """Gets the gamemodes equippables.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[gamemodes.Gamemode]: a list of the gamemodee eqippables
        """
        return await self._handle_request(
            "/gamemodes/equippables",
            list[gamemodes.GamemodeEquippable],
            language=language,
        )

    async def get_gamemode_equippable_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> gamemodes.GamemodeEquippable:
        """Gets a gamemode equippable by its uuid.

        Args:
            uuid (str): the gamemode equippable's uuid
            language (str): the language

        Returns:
            gamemodes.GamemodeEquippable: the gamemode equippable
        """
        return await self._handle_request(
            f"/gamemodes/equippables/{uuid}",
            gamemodes.GamemodeEquippable,
            language=language,
        )

    async def get_gear(self, language: typing.Optional[str] = None) -> list[gear.Gear]:
        """Gets the gear.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[gear.gear]: a list of the gear
        """
        return await self._handle_request("/gear", list[gear.Gear], language=language)

    async def get_gear_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> gear.Gear:
        """Gets a gear by its uuid.

        Args:
            uuid (str): the gear's uuid
            language (str): the language

        Returns:
            gear.gear: the gear
        """
        return await self._handle_request(f"/gear/{uuid}", gear.Gear, language=language)

    async def get_level_borders(
        self, language: typing.Optional[str] = None
    ) -> list[level_borders.LevelBorder]:
        """Gets the level borders.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[level_borders.LevelBorder]: a list of the level borders
        """
        return await self._handle_request(
            "/levelborders", list[level_borders.LevelBorder], language=language
        )

    async def get_level_borders_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> level_borders.LevelBorder:
        """Gets a level border by its uuid.

        Args:
            uuid (str): the level border's uuid
            language (str): the language

        Returns:
            level_borders.LevelBorder: the level border
        """
        return await self._handle_request(
            f"/levelborders/{uuid}", level_borders.LevelBorder, language=language
        )

    async def get_maps(self, language: typing.Optional[str] = None) -> list[maps.Map]:
        """Gets the maps.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[maps.Map]: a list of the maps
        """
        return await self._handle_request("/maps", list[maps.Map], language=language)

    async def get_map_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> maps.Map:
        """Gets a map by its uuid.

        Args:
            uuid (str): the map's uuid
            language (str): the language

        Returns:
            maps.Map: the map
        """
        return await self._handle_request(f"/maps/{uuid}", maps.Map, language=language)

    async def get_player_cards(
        self, language: typing.Optional[str] = None
    ) -> list[player_cards.PlayerCard]:
        """Gets the player cards.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[player_cards.PlayerCard]: a list of the player cards
        """
        return await self._handle_request(
            "/playercards", list[player_cards.PlayerCard], language=language
        )

    async def get_player_card_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> player_cards.PlayerCard:
        """Gets a player card by its uuid.

        Args:
            uuid (str): the player card's uuid
            language (str): the language

        Returns:
            player_cards.PlayerCard: the player card
        """
        return await self._handle_request(
            f"/playercards/{uuid}", player_cards.PlayerCard, language=language
        )

    async def get_player_titles(
        self, language: typing.Optional[str] = None
    ) -> list[player_titles.PlayerTitle]:
        """Gets the player titles.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[player_titles.Playertitle]: a list of the player titles
        """
        return await self._handle_request(
            "/playertitles", list[player_titles.PlayerTitle], language=language
        )

    async def get_player_title_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> player_titles.PlayerTitle:
        """Gets a player title by its uuid.

        Args:
            uuid (str): the player title's uuid
            language (str): the language

        Returns:
            player_titles.Playertitle: the player title
        """
        return await self._handle_request(
            f"/playertitles/{uuid}", player_titles.PlayerTitle, language=language
        )

    async def get_seasons(
        self, language: typing.Optional[str] = None
    ) -> list[seasons.Season]:
        """Gets the seasons.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[seasons.Season]: a list of the seasons
        """
        return await self._handle_request(
            "/seasons", list[seasons.Season], language=language
        )

    async def get_season_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> seasons.Season:
        """Gets a season by its uuid.

        Args:
            uuid (str): the season's uuid
            language (str): the language

        Returns:
            seasons.Season: the season
        """
        return await self._handle_request(
            f"/seasons/{uuid}", seasons.Season, language=language
        )

    async def get_competitive_seasons(
        self, language: typing.Optional[str] = None
    ) -> list[seasons.CompetitiveSeason]:
        """Gets the competitive seasons.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[seasons.CompetitiveSeason]: a list of the competitive seasons
        """
        return await self._handle_request(
            "/seasons/competitive", list[seasons.CompetitiveSeason], language=language
        )

    async def get_competitive_season_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> seasons.CompetitiveSeason:
        """Gets a competitive season by its uuid.

        Args:
            uuid (str): the competitive season's uuid
            language (str): the language

        Returns:
            seasons.CompetitiveSeason: the season
        """
        return await self._handle_request(
            f"/seasons/competitive/{uuid}", seasons.CompetitiveSeason, language=language
        )

    async def get_sprays(
        self, language: typing.Optional[str] = None
    ) -> list[sprays.Spray]:
        """Gets the sprays.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[sprays.Spray]: a list of the sprays
        """
        return await self._handle_request(
            "/sprays", list[sprays.Spray], language=language
        )

    async def get_spray_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> sprays.Spray:
        """Gets a spray by its uuid.

        Args:
            uuid (str): the spray's uuid
            language (str): the language

        Returns:
            sprays.Spray: the spray
        """
        return await self._handle_request(
            f"/sprays/{uuid}", sprays.Spray, language=language
        )

    async def get_spray_levels(
        self, language: typing.Optional[str] = None
    ) -> list[sprays.SprayLevel]:
        """Gets the spray levels.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[sprays.SprayLevel]: a list of the spray levels
        """
        return await self._handle_request(
            "/sprays/levels", list[sprays.SprayLevel], language=language
        )

    async def get_spray_level_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> sprays.Spray:
        """Gets a spray level  by its uuid.

        Args:
            uuid (str): the spray level's uuid
            language (str): the language

        Returns:
            sprays.SprayLevel: the spray level
        """
        return await self._handle_request(
            f"/sprays/levels/{uuid}", sprays.SprayLevel, language=language
        )

    async def get_themes(
        self, language: typing.Optional[str] = None
    ) -> list[themes.Theme]:
        """Gets the themes.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[themes.Theme]: a list of the themes
        """
        return await self._handle_request(
            "/themes", list[themes.Theme], language=language
        )

    async def get_themes_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> themes.Theme:
        """Gets a theme by its uuid.

        Args:
            uuid (str): the theme's uuid
            language (str): the language

        Returns:
            themes.Theme: the theme
        """
        return await self._handle_request(
            f"/themes/{uuid}", themes.Theme, language=language
        )

    async def get_weapons(
        self, language: typing.Optional[str] = None
    ) -> list[weapons.Weapon]:
        """Gets weapons.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[weapons.Weapon]: a list of the weapons
        """
        return await self._handle_request(
            "/weapons", list[weapons.Weapon], language=language
        )

    async def get_weapons_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> weapons.Weapon:
        """Gets a weapon by its uuid.

        Args:
            uuid (str): the weapon's uuid
            language (str): the language

        Returns:
            weapons.Weapon: the weapon
        """
        return await self._handle_request(
            f"/weapons/{uuid}", weapons.Weapon, language=language
        )

    async def get_weapon_skins(
        self, language: typing.Optional[str] = None
    ) -> list[weapons.WeaponSkin]:
        """Gets weapon skins.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[weapons.WeaponSkin]: a list of the weapon skins
        """
        return await self._handle_request(
            "/weapons/skins", list[weapons.WeaponSkin], language=language
        )

    async def get_weapon_skin_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> weapons.WeaponSkin:
        """Gets a weapon skin by its uuid.

        Args:
            uuid (str): the weapon skin's uuid
            language (str): the language

        Returns:
            weapons.WeaponSkin: the weapon skin
        """
        return await self._handle_request(
            f"/weapons/skins/{uuid}", weapons.WeaponSkin, language=language
        )

    async def get_weapon_skin_chromas(
        self, language: typing.Optional[str] = None
    ) -> list[weapons.WeaponSkinChroma]:
        """Gets weapon skin chromas.

        Args:
            language (typing.Optional[str]): the language

        Returns:
            list[weapons.WeaponSkinChroma]: a list of the weapon skin chromas
        """
        return await self._handle_request(
            "/weapons/skinchromas", list[weapons.WeaponSkinChroma], language=language
        )

    async def get_weapon_skin_chroma_by_uuid(
        self, uuid: str, language: typing.Optional[str] = None
    ) -> weapons.WeaponSkinChroma:
        """Gets a weapon skin by its uuid.

        Args:
            uuid (str): the weapon skin's uuid
            language (str): the language

        Returns:
            weapons.WeaponSkinChroma: the weapon skin
        """
        return await self._handle_request(
            f"/weapons/skinchromas/{uuid}", weapons.WeaponSkinChroma, language=language
        )

    async def get_version(self) -> version.Version:
        """Gets the version.

        Returns:
            version.Version: the version
        """
        return await self._handle_request("/version", version.Version)
