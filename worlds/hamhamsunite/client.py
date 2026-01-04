
from worlds._bizhawk.client import BizHawkClient
import worlds._bizhawk as bizhawk
from worlds.hamhamsunite.items import HAMCHATS
from worlds.hamhamsunite.locations import CLUBHOUSE_LOCATION_DATAS


# https://github.com/HaychDeeHD/HamHamsUniteApWorld/tree/main/worlds/_bizhawk

class HamHamsUniteClient(BizHawkClient):
    system = "GBC"
    patch_suffix = (".gbc")
    game = "Ham Hams Unite"

    def __init__(self):
        super().__init__()
        self.checkedDreamingHamsterMegaQ = False
    
    async def validate_rom(self, ctx):
        # This is where I give the server some args it needs (via ctx)
        ctx.game = self.game
        # Indicates I should be sent items from other worlds and from mine
        ctx.items_handling = 0b011

        # TODO In the future, this should determine that the running rom is HHU
        return True
    
    async def set_auth(self, ctx):
        # The client will ask for the player's name unless this function can determine it.
        # TODO in the future, the name could be patched into the ROM and read from there.
        pass

    def on_package(self, ctx, cmd, args):
        # Is this more for system messages like deathlinks and DCs?
        # I think this is not necessary in practice for locs/items if game_watcher is consulting server state
        pass

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
            await ctx.check_locations([locationdata.id for locationdata in CLUBHOUSE_LOCATION_DATAS])

        # These addresses are relative to the start of WRAM, 0xC000

        # TODO generalize this
        byteC76B = (await bizhawk.read(ctx.bizhawk_ctx, [(0x76B, 1, "WRAM")]))[0]
        if not self.checkedDreamingHamsterMegaQ and byteC76B !=  0x00:
            # TODO replace with a location send
            self.checkedDreamingHamsterMegaQ = True
            print('\n\nClient Detected Location Flag!!\n\n')

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
