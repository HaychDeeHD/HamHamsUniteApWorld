from BaseClasses import Location, Region
from .hamchats import HamChatData

# This class represents a location in the multiworld. It will be constructed at generation time.
# This location class only makes sense in a context where there is a defined player and multiworld.
class HamHamsUniteLocation(Location):
    game = "Ham Hams Unite"
    chat: HamChatData

    def __init__(self, chat: HamChatData, player: int, region: Region):
        super().__init__(player, chat.vanilla_location_name, chat.index + 5000, region)
        self.chat = chat

