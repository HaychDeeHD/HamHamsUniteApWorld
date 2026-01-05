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
# If the window contents are in WRAM, I can set them without a patch. --> Might be, but not in player state
# The location flags are being checked instead of the player inventory :(
# And the starting moves don't seem to even be checkign anything? maybe
# Still may be able to manip the window, but the interval could be a problem
# Might require a patch :(

# TODO remove magic numbers/strings

# Bit values
# 0 -- 00000001 -- 0x01
# 1 -- 00000010 -- 0x02
# 2 -- 00000100 -- 0x04
# 3 -- 00001000 -- 0x08
# 4 -- 00010000 -- 0x10
# 5 -- 00100000 -- 0x20
# 6 -- 01000000 -- 0x40
# 7 -- 10000000 -- 0x80

# A dict mapping location_id to location_data
LOCATION_DATA_DICT = create_location_datas([
    ("Starting", "Tutorial HamChat 1 (Hamha)", 0xC919, 3, None),
    ("Starting", "Tutorial HamChat 2 (Tack-Q)", 0xC919, 5, None),
    ("Starting", "Tutorial HamChat 3 (Hif-hif)", 0xC919, 4, None),
    ("Starting", "Tutorial HamChat 4 (Digdig)", 0xC919, 6, None),
    # I don't actually have any way of knowing which bits are which moves, but they're simultaneous.
    ("Starting", "Tutorial HamChat 5 (Scoochie)", 0xC91C, 2, None),
    ("Starting", "Tutorial HamChat 6 (Scrit-T)", 0xC920, 3, None),
    ("Starting", "Tutorial HamChat 7 (Pakapaka)", 0xC920, 4, None),
    ("Starting", "Tutorial HamChat 8 (Go-P)", 0xC920, 5, None),
    ("Starting", "Tutorial HamChat 9 (Lookie)", 0xC921, 3, None),
    ("Starting", "Tutorial HamChat 10 (No-P)", 0xC922, 2, None),
    ("Starting", "Tutorial HamChat 11 (Yep-P)", 0xC922, 3, None),
    ("Acorn Shrine", "Dreaming Hamster (Mega-Q)", 0xC76B, 0, ["Hamha"]),
    ("Acorn Shrine", "Flower Hamster (Koochi-Q)", 0xC91B, 1, ["Hif-hif"]), # TODO this address seems incorrect
    ("Acorn Shrine", "Rooftop Hamster (Nopibloo)", 0xC91D, 4, ["Hamha", "Tack-Q"]),
    ("Acorn Shrine", "Lovesick Hamster (Teenie)", 0xC91A, 4, ["Hamha", "Tack-Q"]),
    ("Acorn Shrine", "Maxwell (Bizarroo)", None, None, ["Nopibloo"]),
    # Oopsie 0xC91D
    # Sparklie 0xC91C
])
