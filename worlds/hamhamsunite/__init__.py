import typing

from BaseClasses import Region
from Utils import visualize_regions
from worlds.generic.Rules import add_rule
from .options import HamHamsUniteGameOptions
from .items import HAMCHATS, HamHamsUniteItem
from .locations import ACORN_SHRINE_LOCATION_DATAS, CLUBHOUSE_LOCATION_DATAS, LOCATION_DATAS, HamHamsUniteLocation
from .settings import HamHamsUniteSettings
from worlds.AutoWorld import World
from .client import HamHamsUniteClient # not used, but must be imported


# from worlds.LauncherComponents import (
#     Component,
#     Type,
#     components,
#     icon_paths,
#     launch_subprocess,
# )


# def run_client() -> None:
#     """
#     Launch Ham-Hams Unite client.
#     """
#     from .KARClient import main

#     launch_subprocess(main, name="KirbyAirRideClient")

# components.append(
#     Component(
#         "Ham Hams Unite Client",
#         # func=run_client,
#         component_type=Type.CLIENT,
#         # icon="Kirby Air Ride",
#     )
# )
# icon_paths["Kirby Air Ride"] = "ap:worlds.kirby_air_ride/assets/allpatch.png"

class MyGameWorld(World):
    """Insert description of the world/game here."""
    game = "Ham Hams Unite"
    options_dataclass = HamHamsUniteGameOptions
    options: HamHamsUniteGameOptions
    settings: typing.ClassVar[HamHamsUniteSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    item_name_to_id = {itemdata.name: itemdata.id for itemdata in HAMCHATS}
    location_name_to_id = {locationdata.name: locationdata.id for locationdata in LOCATION_DATAS}


    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        # TODO Generalize this region creation

        clubhouse_region = Region("Clubhouse", self.player, self.multiworld)
        clubhouse_region.locations = [HamHamsUniteLocation(location_data, self.player, clubhouse_region) for location_data in CLUBHOUSE_LOCATION_DATAS]
        self.multiworld.regions.append(clubhouse_region)


        acorn_shrine_region = Region("Acorn Shrine", self.player, self.multiworld)
        acorn_shrine_region.locations = [HamHamsUniteLocation(location_data, self.player, acorn_shrine_region) for location_data in ACORN_SHRINE_LOCATION_DATAS]
        self.multiworld.regions.append(acorn_shrine_region)


        menu_region.connect(clubhouse_region)
        # TODO may not be 2 way because dig-dig
        clubhouse_region.connect(acorn_shrine_region)


    def create_item(self, name: str) -> HamHamsUniteItem:
        # TODO remove traversal with a map
        for dataitem in HAMCHATS:
            if dataitem.name == name:
                return HamHamsUniteItem(dataitem, self.player)


    def create_items(self) -> None:
        for dataitem in HAMCHATS:
            self.multiworld.itempool.append(self.create_item(dataitem.name))


    def set_rules(self) -> None:

        def has(name):
            return lambda state: state.has(name, self.player)

        # This won't be in the final APWorld except maybe as an alternate win con.
        def has_n_chats(n):
            return lambda state: state.has_from_list_unique([hamchat.name for hamchat in HAMCHATS], self.player, n)


        add_rule(self.multiworld.get_location("Dreaming Hamster (Mega-Q)", self.player), has("Hamha"))
        add_rule(self.multiworld.get_location("Flower Hamster (Koochi-Q)", self.player), has("Hif-hif"))
        add_rule(self.multiworld.get_location("Rooftop Hamster (Nopibloo)", self.player), has("Tack-Q"))
        add_rule(self.multiworld.get_location("Rooftop Hamster (Nopibloo)", self.player), has("Scoochie"))
        # TODO replace the nopibloo requirements with an event (rope) to test that out?
        add_rule(self.multiworld.get_location("Lovesick Hamster (Teenie)", self.player), has("Tack-Q"))
        add_rule(self.multiworld.get_location("Maxwell (Bizarroo)", self.player), has("Tack-Q"))
        add_rule(self.multiworld.get_location("Maxwell (Bizarroo)", self.player), has("Nopibloo"))


        self.multiworld.completion_condition[self.player] = has_n_chats(16)

        # Uncomment to visualize world for debugging
        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

