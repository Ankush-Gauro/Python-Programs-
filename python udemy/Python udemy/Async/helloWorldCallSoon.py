#https://docs.python.org/3.5/library/asyncio-eventloop.html#hello-world-with-call-soon
import asyncio

def hello_world(loop):
    print("Hello World!")
    loop.stop()

loop = asyncio.get_event_loop()

#schedule a call to hello_world
loop.call_soon(hello_world, loop)

#blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
