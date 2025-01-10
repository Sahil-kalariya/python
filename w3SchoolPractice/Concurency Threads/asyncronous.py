import asyncio
import random


async def time_consuming_task():
    print("time-consuming task started")
    try:
        for i in range(1,6):
            await asyncio.sleep(random.randint(1,5))
            print(f"Step {i} completed")
    except asyncio.CancelledError:
        print("time consuming task was cancelled")
        raise


async def  main():
    task = asyncio.create_task(time_consuming_task())
    await asyncio.sleep(random.randint(1,3))
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main coroutine caught task cancellatio")

asyncio.run(main())
    