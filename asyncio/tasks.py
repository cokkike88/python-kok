import asyncio
import time

# In this function we have to wait to finish the firs function (sleep_hello)
# to call the next function (sleep_bye)
async def main():
    await sleep_hello()
    await sleep_bye()

# In this function both function start in the same time :)
async def main_creat_task():
    task_hello = asyncio.create_task(sleep_hello())
    task_bye = asyncio.create_task(sleep_bye())
    task_ciao = asyncio.create_task(sleep_with_timer_ciao())

    # We call each task
    # await task_hello
    # await task_bye

    # We call all task
    await asyncio.wait([task_hello, task_bye, task_ciao])

async def sleep_hello():
    print(f"hello started at {time.strftime('%X')}")
    print('hello')
    await asyncio.sleep(1)
    print('world')
    print(f"hello finished at {time.strftime('%X')}")

async def sleep_bye():
    print(f"bye started at {time.strftime('%X')}")
    print('bye')
    await asyncio.sleep(1)
    print('all')
    print(f"bye finished at {time.strftime('%X')}")

async def sleep_with_timer_ciao():
    print(f"ciao started at {time.strftime('%X')}")
    # 20ms
    # time_to_wait = 20e-5
    # 0.5s
    time_to_wait = 0.5
    intent = 0
    while intent < 5:
        print('ciao', intent)
        intent += 1
        await asyncio.sleep(time_to_wait)
        # Increase double value
        # time_to_wait += time_to_wait
    print('ciao all')
    print(f"ciao finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main_creat_task())