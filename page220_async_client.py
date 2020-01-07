import aiohttp
import asyncio
import os
import aiofiles
async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
        return await res.text()

async def download_html(session, url):
    async with session.get(url, ssl=False) as res:
        filename = 'output/%s.html' % os.path.basename(url)

        async with aiofiles.open(filename, 'wb') as f:
            while True:
                chunk = await res.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)

        return await res.release()

async def main():
    async with aiohttp.ClientSession() as session:
        # situation 1
        html = await get_html(session, 'http://packtpub.com')
        print(html)
        # situation 2
        # await download_html(session, url)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())