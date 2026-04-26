import asyncio
from contextlib import suppress

async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    try:
        f.set_result('I have finished.')
    except RuntimeError as e:
        print(f'No longer allowed: {e}')
        f.cancel()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
future = asyncio.Task(asyncio.sleep(1_000_000))
print(future.done()) #False
loop.create_task(main(future))
# <Task pending name='Task-2' coro=<main() running at <console>:1>>
with suppress(asyncio.CancelledError):
    loop.run_until_complete(future)
# No longer allowed: Task does not support set_result operation

print(future.done()) #True
print(future.cancelled())