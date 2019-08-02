import asyncio

from sphero_sdk import AsyncSpheroRvr
from sphero_sdk import SerialAsyncDal

# Get a reference to the asynchornous program loop
loop = asyncio.get_event_loop()

# Create an AsyncSpheroRvr object, and pass in a SerialAsyncDal object, which in turn takes a reference
# to the asynchronous program loop 
rvr = AsyncSpheroRvr(
    dal=SerialAsyncDal(
        loop
    )
)


async def main():
    """ This program has RVR drive around in different directions using the function drive_with_heading.

    Note:
        To have RVR drive, we call asyncio.sleep(...); if we did not have these calls, the program would
        go on and execute all statements and exit without the driving ever taking place.
    """
    await
    rvr.wake()

    # Reset yaw such that the heading will be set compared to the direction RVR is currently facing
    await
    rvr.reset_yaw()

    # Drive straight for one second at speed 128
    await
    rvr.drive_with_heading(128, 0, 0)
    await
    asyncio.sleep(1)

    # Drive backwards for one second at speed 128
    # Note that the flag is set to 1 for reverse
    await
    rvr.drive_with_heading(128, 0, 1)
    await
    asyncio.sleep(1)

    # Go right for a second (relative to original yaw)
    await
    rvr.drive_with_heading(128, 90, 0)
    await
    asyncio.sleep(1)

    # Go left for a second (relative to original yaw)
    await
    rvr.drive_with_heading(128, 270, 0)
    await
    asyncio.sleep(1)

    # Turn facing the original direction
    await
    rvr.drive_with_heading(0, 0, 0)
    await
    asyncio.sleep(1)

    # Stop RVR
    await
    rvr.raw_motors(0, 0, 0, 0)


# Run event loop until the main function has completed
loop.run_until_complete(
    main()
)

# Stop the event loop
loop.stop()
# Close the event loop
loop.close()
