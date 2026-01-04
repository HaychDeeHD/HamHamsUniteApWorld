
from worlds._bizhawk.client import BizHawkClient
from worlds._bizhawk import display_message, read, write, guarded_write


# https://github.com/HaychDeeHD/HamHamsUniteApWorld/tree/main/worlds/_bizhawk

class HamHamsUniteClient(BizHawkClient):
    system = "GBC"
    patch_suffix = (".gbc")
    game = "Ham Hams Unite"

    def __init__(self):
        super().__init__()
        self.checkedDreamingHamsterMegaQ = False
    
    async def validate_rom(self, ctx):
        # TODO In the future, this should determine that the running rom is HHU
        return True
    
    async def set_auth(self, ctx):
        # The client will ask for the player's name unless this function can determine it.
        # TODO in the future, the name could be patched into the ROM and read from there.
        pass

    def on_package(self, ctx, cmd, args):
        # Is this more for system messages like deathlinks and DCs?
        pass

    async def game_watcher(self, ctx):
        """Runs on a loop with the approximate interval `ctx.watcher_timeout`. The currently loaded ROM is guaranteed
        to have passed your validator when this function is called, and the emulator is very likely to be connected."""
        # if not ctx.server or not ctx.server.socket.open or ctx.server.socket.closed:
        #     return
        
        # data = await read(ctx.bizhawk_ctx, [(loc_data[0], loc_data[1], "WRAM")
        #                                     for loc_data in DATA_LOCATIONS.values()])
        # data = {data_set_name: data_name for data_set_name, data_name in zip(DATA_LOCATIONS.keys(), data)}


        # if data["GameStatus"][0] == 0 or data["ResetCheck"] == b'\xff\xff\xff\x7f':
        #     # Do not handle anything before game save is loaded
        #     self.game_state = False
        #     return
        # elif (data["GameStatus"][0] not in (0x2A, 0xAC)
        #       or data["CrashCheck1"][0] & 0xF0 or data["CrashCheck1"][1] & 0xFF
        #       or data["CrashCheck2"][0]
        #       or data["CrashCheck3"][0] > 10
        #       or data["CrashCheck4"][0] > 3):
        #     # Should mean game crashed
        #     logger.warning("Pokémon Red/Blue game may have crashed. Disconnecting from server.")
        #     self.game_state = False
        #     await ctx.disconnect()
        #     return
        # self.game_state = True


        # await display_message(ctx.bizhawk_ctx, 'Obtained MegaQ ' + str(self.checkedDreamingHamsterMegaQ))

        byteC76B = (await read(ctx.bizhawk_ctx, [(0xC76B, 1, "WRAM")]))[0]
        if not self.checkedDreamingHamsterMegaQ and byteC76B !=  0x00:
            self.checkedDreamingHamsterMegaQ = True
            print('\n\nClient Detected Location Flag!!\n\n')

