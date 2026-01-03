from BaseClasses import Item, ItemClassification

# This class represents an item in the multiworld. It will be constructed at generation time.
# This item class only makes sense in a context where there is a defined player and multiworld.
class HamHamsUniteItem(Item):
    game = "Ham Hams Unite"

    def __init__(self, item_data, player):
        super().__init__(item_data.name, item_data.classification, item_data.id, player)
        self.item_data = item_data

# This is an internal class for defining static item data.
# It is independent of any player or multiworld.
# Instances will be constructed statically in this file. 
# It will only be used by this AP World's own code.
class HamHamsUniteItemData():
    name: str
    id: str
    classification: ItemClassification
    type: str # TODO enum?

    def __init__(self, name, id, classification, type):
        self.name = name
        self.id = id
        self.classification = classification
        self.type = type

class HamChatItemData(HamHamsUniteItemData):
    index: int

    def __init__(self, name, classification, index):
        BASE_HAMCHAT_ID = 1000 # Arbitrary starting id. Avoids id 0.
        super().__init__(name, BASE_HAMCHAT_ID + index, classification, "HamChat")
        self.index = index

# List of all HamChats in the same order the game stores them.
HAMCHATS = [
    HamChatItemData('Hamha', ItemClassification.progression, 0),
    HamChatItemData('Hif-hif', ItemClassification.progression, 1),
    HamChatItemData('Tack-Q', ItemClassification.progression, 2),
    HamChatItemData('Digdig', ItemClassification.progression, 3),
    # HamChatItemData('Nogo', ItemClassification.progression, 4),
    # HamChatItemData('Wondachu', ItemClassification.progression, 5),
    HamChatItemData('Koochi-Q', ItemClassification.progression, 6),
    # HamChatItemData('Grab-b', ItemClassification.progression, 7),
    # HamChatItemData('Hamsolo', ItemClassification.progression, 8),
    HamChatItemData('Teenie', ItemClassification.progression, 9),
    HamChatItemData('Mega-Q', ItemClassification.progression, 10),
    # HamChatItemData('Twintoo', ItemClassification.progression, 11),
    # HamChatItemData('Ouchichi', ItemClassification.progression, 12),
    # HamChatItemData('Spiffie', ItemClassification.progression, 13),
    # HamChatItemData('Blissie', ItemClassification.progression, 14),
    # HamChatItemData('Hamspar', ItemClassification.progression, 15),
    # HamChatItemData('Smoochie', ItemClassification.progression, 16),
    # HamChatItemData('Stickie', ItemClassification.progression, 17),
    # HamChatItemData('Shockie', ItemClassification.progression, 18),
    # HamChatItemData('Frost-T', ItemClassification.progression, 19),
    # HamChatItemData('Noworrie', ItemClassification.progression, 20),
    # HamChatItemData('Blash-T', ItemClassification.progression, 21),
    # HamChatItemData('Krmpkrmp', ItemClassification.progression, 22),
    HamChatItemData('Scoochie', ItemClassification.progression, 23),
    # HamChatItemData('Delichu', ItemClassification.progression, 24),
    # HamChatItemData('Wishie', ItemClassification.progression, 25),
    # HamChatItemData('Blahh', ItemClassification.progression, 26),
    # HamChatItemData('Sparklie', ItemClassification.progression, 27),
    # HamChatItemData('Minglie', ItemClassification.progression, 28),
    # HamChatItemData('Thank-Q', ItemClassification.progression, 29),
    # HamChatItemData('Oopsie', ItemClassification.progression, 30),
    # HamChatItemData('Whawha', ItemClassification.progression, 31),
    # HamChatItemData('Dingbang', ItemClassification.progression, 32),
    HamChatItemData('Nopibloo', ItemClassification.progression, 33),
    # HamChatItemData('Gasp-p', ItemClassification.progression, 34),
    # HamChatItemData('Nokrmp-P', ItemClassification.progression, 35),
    # HamChatItemData('Hammo', ItemClassification.progression, 36),
    # HamChatItemData('Hushie', ItemClassification.progression, 37),
    # HamChatItemData('Zuzuzu', ItemClassification.progression, 38),
    # HamChatItemData('Hushgo', ItemClassification.progression, 39),
    # HamChatItemData('Meep-P', ItemClassification.progression, 40),
    HamChatItemData('Bizzaroo', ItemClassification.progression, 41),
    # HamChatItemData('Wait-Q', ItemClassification.progression, 42),
    # HamChatItemData('Blanko', ItemClassification.progression, 43),
    # HamChatItemData('Lotsa', ItemClassification.progression, 44),
    # HamChatItemData('Ta-dah', ItemClassification.progression, 45),
    # HamChatItemData('Shashaa', ItemClassification.progression, 46),
    # HamChatItemData('Pookie', ItemClassification.progression, 47),
    # HamChatItemData('Herk-Q', ItemClassification.progression, 48),
    # HamChatItemData('Panic-Q', ItemClassification.progression, 49),
    # HamChatItemData('Nopookie', ItemClassification.progression, 50),
    # HamChatItemData('Hulahula', ItemClassification.progression, 51),
    # HamChatItemData('Soak-Q', ItemClassification.progression, 52),
    # HamChatItemData('Grit-T', ItemClassification.progression, 53),
    # HamChatItemData('Hamchu', ItemClassification.progression, 54),
    # HamChatItemData('Goodgo', ItemClassification.progression, 55),
    HamChatItemData('Scrit-T', ItemClassification.progression, 56),
    HamChatItemData('Pakapaka', ItemClassification.progression, 57),
    HamChatItemData('Go-P', ItemClassification.progression, 58),
    # HamChatItemData('Bestest', ItemClassification.progression, 59),
    # HamChatItemData('Hotchu', ItemClassification.progression, 60),
    # HamChatItemData('Cramcram', ItemClassification.progression, 61),
    # HamChatItemData('Clapclap', ItemClassification.progression, 62),
    # HamChatItemData('Chukchuk', ItemClassification.progression, 63),
    HamChatItemData('Lookie', ItemClassification.progression, 64),
    # HamChatItemData('Huffpuff', ItemClassification.progression, 65),
    # HamChatItemData('Perksie', ItemClassification.progression, 66),
    # HamChatItemData('Greatchu', ItemClassification.progression, 67),
    # HamChatItemData('Pooie', ItemClassification.progression, 68),
    # HamChatItemData('Tuggie', ItemClassification.progression, 69),
    # HamChatItemData('Tootru', ItemClassification.progression, 70),
    HamChatItemData('No-P', ItemClassification.progression, 71),
    HamChatItemData('Yep-P', ItemClassification.progression, 72),
    # HamChatItemData('Wit-T', ItemClassification.progression, 73),
    # HamChatItemData('Blushie', ItemClassification.progression, 74),
    # HamChatItemData('Bye-Q', ItemClassification.progression, 75),
    # HamChatItemData('Hamtast', ItemClassification.progression, 76),
    # HamChatItemData('Dundeal', ItemClassification.progression, 77),
    # HamChatItemData('Giftee', ItemClassification.progression, 78),
    # HamChatItemData('See-tru', ItemClassification.progression, 79),
    # HamChatItemData('Bluhoo', ItemClassification.progression, 80),
    # HamChatItemData('Smidgie', ItemClassification.progression, 81),
    # HamChatItemData('Givehoo', ItemClassification.progression, 82),
    # HamChatItemData('Hampact', ItemClassification.progression, 83),
    # HamChatItemData('Gorush', ItemClassification.progression, 84),
    # HamChatItemData('Hamteam', ItemClassification.progression, 85),
]
