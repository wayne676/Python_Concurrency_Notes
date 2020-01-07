import asyncio

class EchoServierClientPortocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport
    
    def connection_lost(self, exc):
        
        print('Connection from {} is lost'.format(exc))

    def data_received(self, data):
        # data includes everything like header, request type, url etc
        message = data.decode()
        print('Data received: {!r}'.format(message))
        # self.transport.write(('\nwocao123123123123123123\n').encode()) no \n then no output
        self.transport.write(('Echoed back: {}'.format(message)).encode())
        # close the transport after the data is sent back to client
        print('Close the client socket')
        self.transport.close()


loop = asyncio.get_event_loop()
# it only initiates the process of creating the server asynchronously, and returns a coroutine that will finish the process.
coro = loop.create_server(EchoServierClientPortocol, '127.0.0.1', 8888)
# run the coroutine, create server. The return value is a Server object which can be used to stop the service.
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()  