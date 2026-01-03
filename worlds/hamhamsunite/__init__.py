import typing
from .options import HamHamsUniteGameOptions
from .items import ham_hams_unite_items
from .locations import ham_hams_unite_locations
from .settings import HamHamsUniteSettings
from worlds.AutoWorld import World


class MyGameWorld(World):
    """Insert description of the world/game here."""
    game = "Hamtaro: Ham-Hams Unite!"
    options_dataclass = HamHamsUniteGameOptions
    options: HamHamsUniteGameOptions
    settings: typing.ClassVar[HamHamsUniteSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # This base_id bizz is pretty unnecessary. Each item/loc def needs a unique id.
    # That can just be part of the item. And there's no reason it can't start at 1.
    # There can be an Item 5 and a Location 5, that's not a conflict.

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 1234
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for
                       id, name in enumerate(ham_hams_unite_items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(ham_hams_unite_locations, base_id)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    # item_name_groups = {
    #     "weapons": {"sword", "lance"},
    # }