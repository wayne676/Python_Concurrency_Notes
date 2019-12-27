'''
For combining async with multi-threading/processing, there is a module called `concurrent.futures`. It is designed to be a high-level
    interface for implementing asynchronous tasks. It provides an abstract class called `Executor` which contains the skeleton of the 
    two main classes that implement asynchronus threading and multiprocessing respectively: 
    ⭐️`ThreadPoolExecutor` and ⭐️`PorcessPoolExecutor`

Chapter 10 example do not really make sense.
Real async and multiprocessing should be something like below:
'''
from concurrent.futures import ProcessPoolExecutor
import asyncio
import time

async def mygen(u: int = 2):
    i = 0
    while i < u:
        yield i
        i += 1

def blocking(delay):
    time.sleep(delay+1)
    return('EXECUTOR: Completed blocking task number ' + str(delay+1))

async def run_blocking(executor, task_no, delay):
    print('MASTER: Sending to executor blocking task number '
          + str(task_no))
    result = await loop.run_in_executor(executor, blocking, delay)
    print(result)
    print('MASTER: Well done executor - you seem to have completed '
          'blocking task number ' + str(task_no))

async def non_blocking(loop):
    tasks = []
    with ProcessPoolExecutor(max_workers=2) as executor:
        # 异步迭代器
        async for i in mygen():
            # spawn the task and let it run in the background
            tasks.append(asyncio.create_task(
                run_blocking(executor, i + 1, i)))
        # if there was an exception, retrieve it now
        await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(non_blocking(loop))
'''
1- get loop
2- pass loop to a coroutine
3- initiate taks queue
4- initiate ProcessPoolExecutor
5- pass tasks into each process or thread
'''
