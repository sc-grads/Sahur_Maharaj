import asyncio
import time


# sync code
def sync_d():
    print(f'1', end='')
    time.sleep(3)
    print('2', end='')


# async
async def ascnc_f():
    print('1', end='')
    await asyncio.sleep(1)  # <-- sim locking io
    print('2', end='')


async def main():
    # Note that there are 3 awaitable objects: coroutines, tasks and futures.
    tasks = [ascnc_f() for _ in range(3)]

    # we schedule the coroutines to run asap by gathering the tasks like this:
    await asyncio.gather(*tasks)


s = time.time()

asyncio.run(main())  # prints out: one one one two two two and takes 1 second
print(f'Execution time (ASYNC):{time.time() - s}')

print('\n')

s = time.time()
for _ in range(3):
    sync_d()  # prints out: one two one two one two and takes 3 seconds
print(f'Execution time (SYNC):{time.time() - s}')


# async def f():
#     pass
#
# async def g():
#     await f()
