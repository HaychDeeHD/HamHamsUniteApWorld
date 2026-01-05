from typing import List, Optional
from BaseClasses import Location

# This class represents a location in the multiworld. It will be constructed at generation time.
# This location class only makes sense in a context where there is a defined player and multiworld.
class HamHamsUniteLocation(Location):
    game = "Ham Hams Unite"

    def __init__(self, location_data, player, region):
        super().__init__(player, location_data.name, location_data.id, region)
        self.location_data = location_data


# This is an internal class for defining static location data.
# It is independent of any player or multiworld.
# Instances will be constructed statically in this file. 
# It will only be used by this AP World's own code.
class HamHamsUniteLocationData():
    id: str
    region_name: str
    name: str
    address: Optional[int]
    bit: Optional[int]
    required_items: List[str]
    # classification: ItemClassification
    # type: str # TODO enum?

    def __init__(self, id, region_name, name, address, bit, required_items):
        self.id = id
        self.region_name = region_name
        self.name = name
        self.address = address
        self.bit = bit
        self.required_items = required_items or []


def create_location_datas(location_tuple_list):
     BASE_LOC_ID = 1000 # Arbitrary starting id for locations. Helps avoid id 0.
     return {BASE_LOC_ID + id: HamHamsUniteLocationData(BASE_LOC_ID + id, *tuple) for id, tuple in enumerate(location_tuple_list)}

# TODO can't safely connect until after Boss tutorial
# TODO The game is letting me use moves I did not collect
# Is it just starting moves?
# If the window contents are in WRAM, I can set them without a patch.
# Or if there is some other part of state that is consulted (tutorial may be a clue)
# Need to revisit the tutorial anyway
# TODO remove magic numbers/strings

# A dict mapping location_id to location_data
LOCATION_DATA_DICT = create_location_datas([
    ("Starting", "Boss Starting HamChat 1", None, None, None),
    ("Starting", "Boss Starting HamChat 2", None, None, None),
    ("Starting", "Boss Starting HamChat 3", None, None, None),
    ("Starting", "Boss Starting HamChat 4", None, None, None),
    ("Starting", "Boss Starting HamChat 5", None, None, None),
    ("Starting", "Boss Starting HamChat 6", None, None, None),
    ("Starting", "Boss Starting HamChat 7", None, None, None),
    ("Starting", "Boss Starting HamChat 8", None, None, None),
    ("Starting", "Boss Starting HamChat 9", None, None, None),
    ("Starting", "Boss Starting HamChat 10", None, None, None),
    ("Starting", "Boss Starting HamChat 11", None, None, None),
    ("Acorn Shrine", "Dreaming Hamster (Mega-Q)", 0xC76B, 0, ["Hamha"]),
    ("Acorn Shrine", "Flower Hamster (Koochi-Q)", 0xC91B, 1, ["Hif-hif"]), # TODO this address seems incorrect
    ("Acorn Shrine", "Rooftop Hamster (Nopibloo)", None, None, ["Hamha", "Tack-Q"]),
    ("Acorn Shrine", "Lovesick Hamster (Teenie)", 0xC91A, 4, ["Hamha", "Tack-Q"]),
    ("Acorn Shrine", "Maxwell (Bizarroo)", None, None, ["Nopibloo"]),
])
