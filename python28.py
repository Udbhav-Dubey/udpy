import asyncio

async def main():
    await func()

async def func():
    print("hello,async world!")

asyncio.run(main())
