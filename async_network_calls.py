import time
import asyncio
import aiohttp

async def make_request(session, req_n):
    print(f"make request {req_n+1}")
    async with session.get(f'https://httpbin.org/get') as resp:
        if resp.status == 200:
             await resp.json()

async def main():
    request_count = 10
    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, req_n) for req_n in range(request_count)]
        await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
start_time = time.time()
loop.run_until_complete(main())
end_time = time.time()
print(f"total time: {end_time - start_time}")