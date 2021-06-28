#Versão 3.5
#https://docs.python.org/3.5/library/asyncio-eventloop.html#hello-world-with-call-soon
import asyncio

async def hello_world():
    print("Hello World!")

loop = asyncio.get_event_loop()

#blocking call which returns when hello_world() coroutine is done
loop.run_until_complete(hello_world())
loop.close()