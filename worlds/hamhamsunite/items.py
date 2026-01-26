from BaseClasses import Item, ItemClassification
from .hamchats import HamChatData

# This class represents an item in the multiworld. It will be constructed at generation time.
# This item class only makes sense in a context where there is a defined player and multiworld.
class HamHamsUniteItem(Item):
    game = "Ham Hams Unite"
    chat: HamChatData

    # TODO This shouldn't be HamChat specific
    def __init__(self, chat: HamChatData, player: int):
        # TODO not all progression. Determine using requirements.
        # TODO remove magic 1000. Make an index -> id function.
        super().__init__(chat.name, ItemClassification.progression, chat.index + 1000, player)
        self.chat = chat

