
from worlds._bizhawk.client import BizHawkClient
import worlds._bizhawk as bizhawk
from worlds.hamhamsunite.items import HAMCHATS
from worlds.hamhamsunite.locations import LOCATION_DATA_DICT


# https://github.com/HaychDeeHD/HamHamsUniteApWorld/tree/main/worlds/_bizhawk

class HamHamsUniteClient(BizHawkClient):
    system = "GBC"
    patch_suffix = (".gbc")
    game = "Ham Hams Unite"


    async def validate_rom(self, ctx):
        # This is where I give the server some args it needs (via ctx)
        ctx.game = self.game
        # Indicates I should be sent items from other worlds and from mine
        ctx.items_handling = 0b011

        # TODO In the future, this should determine that the running rom is HHU
        return True


    async def game_watcher(self, ctx):
        # Require a server connection
        if not ctx.server or not ctx.server.socket.open or ctx.server.socket.closed:
            return

        await self.update_checked_locations(ctx)
        await self.write_inventory_from_state(ctx)


    async def update_checked_locations(self, ctx):
        # If there are no checked locations in state, we auto-check Boss's gift Chats as starting checks
        # TODO in the future there may be flags representing these
        if len(ctx.checked_locations) == 0:
            await ctx.check_locations([location_data.id for location_data in LOCATION_DATA_DICT.values() if location_data.region_name == "Starting"])
            return

        # All these addresses are relative to the start of WRAM, 0xC000.

        # Read bytes C718 - CAB5 (inclusive). 922 state bytes plus 4 ending bytes
        player_state = list((await bizhawk.read(ctx.bizhawk_ctx, [(0x718, 926, "WRAM")]))[0])

        def getByte(address):
            return player_state[address - 0xC718]

        def getBit(address, bit):
            return bool(getByte(address) & (1 << bit))

        newly_checked_locations = []
        for location_id in ctx.missing_locations:
            location_data = LOCATION_DATA_DICT[location_id] # Throws KeyError if not found? 
            if location_data.address != None and location_data.bit != None and getBit(location_data.address, location_data.bit):
                newly_checked_locations.append(location_id)

        if len(newly_checked_locations) > 0:
            await ctx.check_locations(newly_checked_locations)


    async def write_inventory_from_state(self, ctx):
        chatarray = [0xFF] * 2 * 86
        for collect_order, received in enumerate(ctx.items_received):
            # TODO Replace traversal with a map
            # TODO in the future, misses will be expected because not all items will be hamchats
            hamchatitemdata = next((itemdata for itemdata in HAMCHATS if itemdata.id == received.item)) # TODO may throw ValueError
            chatarray[hamchatitemdata.index * 2] = collect_order
        num_chats = len(ctx.items_received) # TODO in the future there will be other items
        chatarray.append(num_chats)

        await bizhawk.write(ctx.bizhawk_ctx, [(0x9A3, chatarray, "WRAM")])
