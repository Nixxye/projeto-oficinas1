import asyncio

class T_class:
    end = False

    def __init__(self):
        pass

    @classmethod
    def close(cls):
        cls.end = True

    async def run(self):
        pass

