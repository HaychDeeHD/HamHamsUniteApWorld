import typing

from BaseClasses import Region
from worlds.generic.Rules import add_rule
from .options import HamHamsUniteGameOptions
from .items import HAMCHATS, HamHamsUniteItem
from .locations import LOCATION_DATA_DICT, HamHamsUniteLocation
from .settings import HamHamsUniteSettings
from worlds.AutoWorld import World
from .client import HamHamsUniteClient # not used, but must be imported


class HamHamsUniteWorld(World):
    """Insert description of the world/game here."""
    game = "Ham Hams Unite"
    options_dataclass = HamHamsUniteGameOptions
    options: HamHamsUniteGameOptions
    settings: typing.ClassVar[HamHamsUniteSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    item_name_to_id = {itemdata.name: itemdata.id for itemdata in HAMCHATS}
    location_name_to_id = {location_data.name: location_data.id for location_data in LOCATION_DATA_DICT.values()}


    def create_regions(self) -> None:
        name_to_region_dict = {}
        def getOrCreateRegion(name):
            existing_region = name_to_region_dict.get(name)
            if existing_region:
                return existing_region
            new_region = Region(name, self.player, self.multiworld)
            name_to_region_dict[name] = new_region
            self.multiworld.regions.append(new_region)
            return new_region

        getOrCreateRegion("Menu")
        for location_data in LOCATION_DATA_DICT.values():
            location_region = getOrCreateRegion(location_data.region_name)
            location_region.locations.append(HamHamsUniteLocation(location_data, self.player, location_region))

        def connect_regions(name1, name2):
            region1 = name_to_region_dict.get(name1)
            region2 = name_to_region_dict.get(name2)
            if region1 and region2:
                region1.connect(region2)
                # TODO else throw?

        connect_regions("Menu", "Starting")
        # TODO may not be 2 way because dig-dig
        connect_regions("Starting", "Acorn Shrine")


    def create_item(self, name: str) -> HamHamsUniteItem:
        # TODO remove traversal with a map
        for dataitem in HAMCHATS:
            if dataitem.name == name:
                return HamHamsUniteItem(dataitem, self.player)


    def create_items(self) -> None:
        for dataitem in HAMCHATS:
            self.multiworld.itempool.append(self.create_item(dataitem.name))


    def set_rules(self) -> None:
        for location in self.get_locations():
            for required_item in location.location_data.required_items:
                add_rule(location, lambda state: state.has(required_item, self.player))

        # This won't be in the final APWorld except maybe as an alternate win con.
        def has_n_chats(n):
            return lambda state: state.has_from_list_unique([hamchat.name for hamchat in HAMCHATS], self.player, n)
        self.multiworld.completion_condition[self.player] = has_n_chats(16)
