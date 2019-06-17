# -*- coding: utf-8 -*-

import asyncio

from geolite2 import geolite2

from aioli.service import BaseService
from aioli_rdbms import DatabaseService

from .. import database


class VisitorService(BaseService):
    geoip = geolite2.reader()
    db = None

    async def on_unit_ready(self):
        self.db = self.attach_service(DatabaseService).use_model(database.VisitorModel)

    async def ipaddr_location(self, value):
        def in_english(*locations):
            for loc in locations:
                yield loc["names"]["en"]

        loop = asyncio.get_running_loop()
        geoip = await loop.run_in_executor(None, self.geoip.get, value)

        if value in ["127.0.0.1", "::1"]:
            return "Localhost", "Localdomain"
        if not geoip:
            return "Unknown City", "Unknown Country"

        return in_english(geoip["city"], geoip["country"])
