from aqman.aqman import Aqman
from aqman.models import DeviceState
import asyncio

ID = ''
PASSWORD = ''
DEVICEID = ''


async def main():
    """Show example on controlling your Elgato Key Light device."""
    async with Aqman(ID, PASSWORD, DEVICEID) as aqman:
        state: DeviceState = await aqman.state()
        print(state)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
