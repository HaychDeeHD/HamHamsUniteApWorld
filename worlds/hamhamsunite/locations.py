from BaseClasses import Location

# This class represents a location in the multiworld. It will be constructed at generation time.
# This location class only makes sense in a context where there is a defined player and multiworld.
class HamHamsUniteLocation(Location):
    game = "Ham Hams Unite"

    def __init__(self, location_data, player, region):
        super().__init__(player, location_data.name, location_data.id, region)
        self.location_data = location_data


# This is an internal class for defining static item data.
# It is independent of any player or multiworld.
# Instances will be constructed statically in this file. 
# It will only be used by this AP World's own code.
class HamHamsUniteLocationData():
    name: str
    id: str
    # classification: ItemClassification
    # type: str # TODO enum?

    def __init__(self, name, id):
        self.name = name
        self.id = id 
        # self.classification = classification
        # self.type = type

# TODO in the future, subclasses may be helpful


def create_location_datas(location_name_list, base_id):
    return [HamHamsUniteLocationData(name, base_id + id) for id, name in enumerate(location_name_list)]

CLUBHOUSE_LOCATION_DATAS = create_location_datas([
    "Boss Starting HamChat 1",
    "Boss Starting HamChat 2",
    "Boss Starting HamChat 3",
    "Boss Starting HamChat 4",
    "Boss Starting HamChat 5",
    "Boss Starting HamChat 6",
    "Boss Starting HamChat 7",
    "Boss Starting HamChat 8",
    "Boss Starting HamChat 9",
    "Boss Starting HamChat 10",
    "Boss Starting HamChat 11",
], 1000)

ACORN_SHRINE_LOCATION_DATAS = create_location_datas([
    "Dreaming Hamster (Mega-Q)",
    "Flower Hamster (Koochi-Q)",
    "Rooftop Hamster (Nopibloo)",
    "Lovesick Hamster (Teenie)",
    "Maxwell (Bizarroo)",
    # Maxwell, Friend
], 2000)

LOCATION_DATAS = CLUBHOUSE_LOCATION_DATAS + ACORN_SHRINE_LOCATION_DATAS
