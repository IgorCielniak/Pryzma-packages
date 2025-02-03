async def interpret2(self, func):
    import asyncio
    await asyncio.to_thread(self.interpret, func)

async def interpret(self, line):
    import asyncio
    await asyncio.gather(interpret2(self, line[0]), interpret2(self, line[1]))


async def run_interpret(self, line):
    import asyncio
    await interpret(self, line)

def aasync(self, func1, func2):
    import asyncio
    line = [func1, func2]
    asyncio.run(run_interpret(self, line))
