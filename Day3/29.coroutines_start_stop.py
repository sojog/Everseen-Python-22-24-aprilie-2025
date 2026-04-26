async def f():
    return 123

coro = f()

try:
    coro.send(None) # A coroutine is initiated by “sending” it a None.
except StopIteration as e:
    print('The answer was:', e.value) # When the coroutine returns, a special kind of exception is raised, called StopIteration.
    
# All the coroutines you make will be executed either with loop.create_task(coro) or await coro. It’s the loop that does the .send(None) behind the scenes.
## These two points, the send() and the StopIteration, define the start and end of the executing coroutine, respectively