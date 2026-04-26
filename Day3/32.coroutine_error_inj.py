import asyncio


async def f():
    await asyncio.sleep(1.0) # Calling f() produces a coroutine; this means we are allowed to await it. The value of the result variable will be 123 when f()completes.
    return 123

# when you call task.cancel(), the event loop will internally use coro.throw() to raise asyncio.CancelledError inside your coroutine
coro = f() # a new coroutine is created from the coroutine function f().
coro.send(None) # Instead of doing another send(), we call throw() and provide an exception class and a value. This raises an exception inside our coroutine, at the await point.
coro.throw(Exception, 'whatever')

print("After the error")