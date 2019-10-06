import requests
import asyncio


async def printRequest():
    r = requests.get(url='https://swapi.co/api/people/')
    print(r.json())


async def main():
    await asyncio.gather(
        printRequest
    )
asyncio.run(main())
