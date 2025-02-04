import asyncio
from bleak import BleakClient, BleakScanner
from aiohttp import web

class HomeHub:
    def __init__(self):
        self.devices = {}
        
    async def discover_devices(self):
        scanner = BleakScanner()
        devices = await scanner.discover()
        for d in devices:
            if 'SmartBulb' in d.name:
                self.devices[d.address] = {'type': 'light', 'client': BleakClient(d.address)}
    
    async def control_device(self, device_id, action):
        async with self.devices[device_id]['client'] as client:
            if self.devices[device_id]['type'] == 'light':
                await client.write_gatt_char("0000ffe1-0000-1000-8000-00805f9b34fb", 
                                           bytearray([0x7E, 0x00, 0x04, action, 0xEF]))
    
    async def web_interface(self):
        app = web.Application()
        app.add_routes([web.get('/control/{device}/{action}', self.handle_control)])
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', 8080)
        await site.start() 