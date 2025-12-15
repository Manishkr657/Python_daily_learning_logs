import asyncio
import aiofiles

file = "myfile.json"

async def read_file():
    async with aiofiles.open(file,"r") as f:
        content = await f.read()
        