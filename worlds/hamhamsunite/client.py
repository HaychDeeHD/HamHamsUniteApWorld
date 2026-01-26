from worlds._bizhawk.client import BizHawkClient
import worlds._bizhawk as bizhawk
# from worlds.hamhamsunite.locations import LOCATION_DATA_DICT

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

# https://github.com/HaychDeeHD/HamHamsUniteApWorld/tree/main/worlds/_bizhawk

def getBitArrayByteAndBit(bitArrayIndex: int) -> tuple[int, int]:
    bitArrayByteAddress = 0xC918 + (bitArrayIndex // 8)
    bitArrayBitNumber = bitArrayIndex % 8
    return (bitArrayByteAddress, bitArrayBitNumber)

class HamHamsUniteClient(BizHawkClient):
    system = "GBC"
    patch_suffix = (".gbc")
    game = "Ham Hams Unite"


    async def validate_rom(self, ctx: 'BizHawkClientContext'):
        # This is where I give the server some args it needs (via ctx)
        ctx.game = self.game
        # Indicates I should be sent items from other worlds and from mine
        ctx.items_handling = 0b011

        # TODO In the future, this should determine that the running rom is HHU
        return True


    async def game_watcher(self, ctx: 'BizHawkClientContext'):
        # Require a server connection
        if not ctx.server or not ctx.server.socket.open or ctx.server.socket.closed: # pyright: ignore[reportUnknownMemberType]
            return

        await self.update_checked_locations(ctx)
        await self.write_hambook_from_state(ctx)


    async def update_checked_locations(self, ctx: 'BizHawkClientContext'):
        # TODO implement starting_items

        # All these addresses are relative to the start of WRAM, 0xC000.

        # Read bytes C718 - CAB5 (inclusive). 922 state bytes plus 4 ending bytes
        player_state = list((await bizhawk.read(ctx.bizhawk_ctx, [(0x718, 926, "WRAM")]))[0])

        def isLocationChecked(location_id: int) -> bool:
            # TODO In the future there will be non-chat locations. Also remove the magic number.
            bitArrayIndex = location_id - 5000 + 11 # The first Hamchat is at index 11
            bitArrayByteAddress, bitArrayBitNumber = getBitArrayByteAndBit(bitArrayIndex)
            return bool(player_state[bitArrayByteAddress - 0xC718] & (1 << bitArrayBitNumber))

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # TODO this isn't going to work. We can't read location flags from the same place we write item flags!
        # I guess we will need to find other flags that indicate you got the chat? Like the giving hamster's state? What we were starting to track before.
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        newly_checked_locations: List[int] = [location_id for location_id in ctx.missing_locations if isLocationChecked(location_id)]
        if len(newly_checked_locations) > 0:
            await ctx.check_locations(newly_checked_locations)


    async def write_hambook_from_state(self, ctx: 'BizHawkClientContext'):
        chatarray = [0xFF] * 2 * 86
        for collect_order, received in enumerate(ctx.items_received):
            # TODO In the future there will be non-chat locations. Also remove the magic number.
            chatarray[(received.item - 1000) * 2] = collect_order
        num_chats = len(ctx.items_received) # TODO in the future there will be other items
        chatarray.append(num_chats)

        await bizhawk.write(ctx.bizhawk_ctx, [(0x9A3, chatarray, "WRAM")])

    async def write_bitarray_obtained_hamchat_flags_from_state(self, ctx: 'BizHawkClientContext'):
        # TODO don't overwrite the non-Chat flags on the ends with 0's
        chats_bitarray = [0x00] * 13
        for item in ctx.items_received:
            # TODO In the future there will be non-chat locations. Also remove the magic number.
            bitArrayIndex = item.item - 1000 + 11 # The first Hamchat is at index 11
            bitArrayByteAddress, bitArrayBitNumber = getBitArrayByteAndBit(bitArrayIndex)
            chats_bitarray_index = bitArrayByteAddress - 0xC918
            # Flip bit from 0 to 1
            chats_bitarray[chats_bitarray_index] = chats_bitarray[chats_bitarray_index] | (1 << bitArrayBitNumber)

        await bizhawk.write(ctx.bizhawk_ctx, [(0x918, chats_bitarray, "WRAM")])
