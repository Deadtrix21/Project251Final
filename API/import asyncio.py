import asyncio


class dbConnect1:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        print("hello")
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass


class dbConnect2:
    def __init__(self):
        self.connection = None

    async def __aenter__(self):
        print("hello")
        return "hello"

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        pass


async def main():
    async with dbConnect2() as e:
        print(e)


asyncio.run(main())
