# ch10/example2.py

import asyncio
import time

async def count_down(name, delay):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        await asyncio.sleep(delay)

        duration = time.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -= 1

loop = asyncio.get_event_loop() # ⭐️1 returns the event loop for the current context
tasks = [
    loop.create_task(count_down('A', 1)),
    loop.create_task(count_down('B', 0.8)),
    loop.create_task(count_down('C', 0.5))
] # ⭐️2 adds coroutine into task queue.

start = time.perf_counter()
loop.run_until_complete(asyncio.wait(tasks)) # ⭐️3 & ⭐️6

print('-' * 40)
print('Done.')

'''
⭐️1- asyncio.get_event_loop(): It is an AbstractEventLoop object. It returns the event loop for the current context.
⭐️2- AbstractEventLoop.create_task(): Adds its input to the current task queue of the calling event loop; typically input is a coroutine
⭐️3- AbstractEventLoop.run_until_complete(): It takes in the main coroutine of an asynchronous program and executes it until the 
    corresponding future of the coroutine is returned. While the method initiates the event loop execution, it also blocks all 
    subsequent code following it until all futures are `complete`.
⭐️4- AbstractEventLoop.run_forever(): the calling event loop will run forever unless the AbstractEventLoop.stop() is called.
⭐️5- AbstractEventLoop.stop(): Causes the callling event loop to stop executing and exit at the nearest appropriate oportunity without
    causing the whole program to crash.
⭐️6 - asyncio.wait(): Itself is a coroutine. It takes in a sequence (usually a list) of futures and waits for them to complete 
    their execution.
'''