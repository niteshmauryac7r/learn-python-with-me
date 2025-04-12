import time
import asyncio
import requests


async def function1():
    url = 'https://images.unsplash.com/photo-1624555130581-1d9cca783bc0?q=80&w=2942&auto=format&fit=' \
    'crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    start = time.time()
    print("Starting Download 1")
    r = requests.get(url, allow_redirects=True)
    open('google.jpg', 'wb').write(r.content)
    await asyncio.sleep(1)
    print("Finished Download 1")
    end = time.time()
    total = end - start
    return total

async def function2():
    url = 'https://images.unsplash.com/photo-1624555130581-1d9cca783bc0?q=80&w=2942&auto=format&fit=crop&ixl' \
    'ib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    start = time.time()
    print("Starting Download 2")
    r = requests.get(url, allow_redirects=True)
    open('google2.jpg', 'wb').write(r.content)
    await asyncio.sleep(1)
    print("Finished Download 2")
    end = time.time()
    total = end - start
    return total

async def function3():
    url = 'https://images.unsplash.com/photo-1624555130581-1d9cca783bc0?q=80&w=2942&auto=format&fit' \
    '=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    start = time.time()
    print("Starting Download 3")
    r = requests.get(url, allow_redirects=True)
    open('google3.jpg', 'wb').write(r.content)
    await asyncio.sleep(1)
    print("Finished Download 3")
    end = time.time()
    total = end - start
    return total

async def function4():
    start = time.time()
    print("Starting Download 4")
    await asyncio.sleep(4)
    print("Finished Download 4")
    end = time.time()
    total = end - start
    return total

async def main():
    # #task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()
    # await function4()
    # return 1
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
        function4()
    )
    print(L)
asyncio.run(main())