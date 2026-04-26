
# A Futureure represents a futureure completion state of some activity and is managed by the loop.
# A Task is exactly the same, but the specific “activity” is a coroutine
# The Futureure class is actually a superclass of Task, and it provides all of the functionality for interaction with the loop.


import asyncio

async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    f.set_result('I have finished.')

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


future = asyncio.Future()
print("Is it done?:", future.done())

loop.create_task(main(future))
## <Task pending name='Task-1' coro=<main() running at <console>:1>>
loop.run_until_complete(future)
## 'I have finished.'
print(future.done()) 
# True
print(future.result())