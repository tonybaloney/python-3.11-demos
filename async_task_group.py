import asyncio


async def connect(server: str, port: 1234):
    ...

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(connect("localhost", 1234))
            tg.create_task(connect("localhost", 4356))
    except* OSError as eg:
        # Handle exception group
        ...
